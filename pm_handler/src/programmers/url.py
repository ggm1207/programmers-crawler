"""
Problem
"""
import requests

from pm_handler.src.const import GOOD, BAD


def is_valid_url(programmers_url: str):
    """ check the url's status_code is 200 """
    response = requests.get(programmers_url)
    return response.status_code == 200


class Url:
    """ 사용자가 입력한 문제를 파싱할 수 있는지 판단합니다. """

    support = ["c", "cpp", "csharp", "java", "javascript", "kotlin", "python3", "swift"]

    def __init__(self, problem_num, language):
        self._language: str = language
        self._url: str = (
            f"https://programmers.co.kr/learn/courses"
            f"/30/lessons/{problem_num}?language={language}/"
        )
        self._is_valid_language()
        self._is_valid_url(problem_num)

        self.status: int = GOOD
        self.msg: str = None

    def _is_valid_url(self, problem_num):
        """ check the url's status_code is 200 """
        if not is_valid_url(self._url):
            self.msg = (
                f"{problem_num}번의 {self._language}언어를 사용하는 문제는 없는 문제이므로 파싱할 수 없습니다."
            )
            self.status = BAD

    def _is_valid_language(self):
        """ check the language's support """
        if self.language not in self.support:
            self.status = BAD
            raise ValueError(f"{self.language}: 지원하지 않는 언어입니다.")


if __name__ == "__main__":
    p = Url("68646", "cpp")
