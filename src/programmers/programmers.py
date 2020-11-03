import os
import time
from pathlib import Path

from testcase import TestCase
from solution import Solution


class Programmers:
    def __init__(self, driver, cfg: dict):
        self.url = "https://programmers.co.kr/learn/courses/30/lessons/{}/"
        self.driver = driver
        self.testcase = TestCase()
        self.solution = Solution()
        self.cfg = cfg
        self._login()

    def _login(self):
        self.driver.get("https://programmers.co.kr/")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/ul[2]/li[2]/a").click()
        LOGIN_SELECT = self.cfg["login_select"]
        self._id, self._pw = [line.strip("\n") for line in open("./user_info")][:2]

        print(self._id, self._pw)

        if LOGIN_SELECT == 0:
            self._common_login()
        elif LOGIN_SELECT == 1:
            self._facebook_login()
        elif LOGIN_SELECT == 2:
            self._github_login()

    def _common_login(self):
        self.driver.find_element_by_id("user_email").send_keys(self._id)
        self.driver.find_element_by_id("user_password").send_keys(self._pw)
        self.driver.find_element_by_id("btn-sign-in").click()

    def _facebook_login(self):
        self.driver.find_element_by_id("logo-facebook").click()  # use logo id
        try:
            self.driver.find_element_by_id("email").send_keys(self._id)
            self.driver.find_element_by_id("pass").send_keys(self._pw)
            self.driver.find_element_by_id("loginbutton").click()
        except:
            pass

    def _github_login(self):
        self.driver.find_element_by_id("logo-github").click()  # use logo id
        try:
            self.driver.find_element_by_id("login_field").send_keys(self._id)
            self.driver.find_element_by_id("password").send_keys(self._pw)
            self.driver.find_element_by_xpath(
                '//*[@id="login"]/form/div[3]/input[12]'
            ).click()
        except:
            pass

    def _path_prepare(self, lang: str, problem: str):
        save_path = Path(os.path.abspath(self.cfg["save_path"]))
        save_path = save_path / lang
        save_path.mkdir(parents=True, exist_ok=True)
        save_path = save_path / problem
        save_path.touch()
        return save_path

    def _write(self, save_path):
        if os.path.exists(save_path):
            print(f"{save_path} Already Exist")
            return

        self.solution.write(save_path)
        self.testcase.write(save_path)

    def _parsing(self, languages, problem):
        self.driver.find_element_by_link_text("테스트 케이스 추가하기").click()
        self.testcase.parsing(self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="applicant-testcase-modal"]/div/div[1]/button'
        ).click()

        for lang in languages:
            self.driver.find_element_by_css_selector("#tour7 > button").click()
            self.driver.find_element_by_link_text(lang).click()

            save_path = self._path_prepare(lang, problem)

            solution_content = self.driver.find_element_by_css_selector(
                "#tour3 > div > div"
            ).text
            self.solution.parsing(solution_content)
            self.testcase.select_language(lang)

            self._write(save_path)

    def parsing(self, problems):
        for i, problem in enumerate(problems):
            url = self.url.format(problem)
            self.driver.get(url)
            if i == 0:  # Tutorial skip
                self.driver.find_element_by_css_selector(
                    "#step-0 > div:nth-child(3) > svg"
                ).click()
            self._parsing(self.cfg["languages"], problem)


if __name__ == "__main__":
    from driver import Driver

    d = Driver()
    config = {"languages": ["C++"], "select": [1, 1, 0], "save_path": "."}
    config.update({"login_select": 1})

    p = Programmers(d, config)
    p.parsing(["68646"])
