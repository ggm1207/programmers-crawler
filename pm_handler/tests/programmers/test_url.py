import unittest

from pm_handler.src.programmers.url import Url


class TestURl(unittest.TestCase):
    def test_url_status_200(self):
        url = Url("68646", "cpp")
        self.assertEqual(url.msg, None)

    def test_url_status_bad(self):
        url = Url("78646", "cpp")
        print("msg:", url.msg)
        self.assertNotEqual(url.msg, None)
