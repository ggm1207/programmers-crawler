from time import sleep

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException


class Driver:
    def __init__(self, driver_path=None, headless=None):
        driver_path = driver_path or "/home/j-gunmo/chromedriver_linux64/chromedriver"
        op = webdriver.ChromeOptions()
        if headless:
            op.add_argument("headless")
        op.add_argument("--window-size=1920,1080")
        op.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)",
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100",
            "Safari/537.36",
        )
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "disk-cache-size": 4096,
        }
        op.add_experimental_option("prefs", prefs)

        try:
            self.driver = webdriver.Chrome(driver_path, options=op)
            self.driver.implicitly_wait(5)
        except SessionNotCreatedException as e:
            print("Check the ChromeDriver Version..: ", e)

    def get(self, url):
        while self.driver.current_url != url:
            print(self.driver.current_url, url)
            self.driver.get(url)
            sleep(1)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def find_elements_by_css_selector(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def find_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_element_by_id(self, keyid):
        return self.driver.find_element_by_id(keyid)

    def find_elements_by_class_name(self, classname):
        return self.driver.find_elements_by_class_name(classname)
