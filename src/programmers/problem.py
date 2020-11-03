"""
Problem
"""

import requests


def is_valid_url(programmers_url: str):
    """ check the url's status_code is 200 """
    response = requests.get(programmers_url)
    return response.status_code == 200


class Problem:
    """ 사용자가 입력한 문제를 파싱할 수 있는지 판단합니다. """

    support = ["c", "cpp", "csharp", "java", "javascript", "kotlin", "python3", "swift"]

    def __init__(self, problem_num, language):
        self.language = language
        self.url = problem_num
        self._language = None
        self._url = None
        self.msg = None

    @property
    def url(self):
        """ return url """
        return self._url

    @url.setter
    def url(self, problem_num):
        """ check the url's status_code is 200 """
        self._url = (
            f"https://programmers.co.kr/learn/courses"
            f"/30/lessons/{problem_num}?language={self.language}/"
        )
        if not is_valid_url(self._url):
            self.msg = (
                f"{problem_num}번의 {self.language}언어를 사용하는 문제는 없는 문제이므로 파싱할 수 없습니다."
            )

    @property
    def language(self):
        """ return language """
        return self._language

    @language.setter
    def language(self, language):
        """ check the language's support """
        if language not in self.support:
            raise ValueError("{language}: 지원하지 않는 언어입니다.")
        self._language = language
