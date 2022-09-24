import time
from pages.home.login_page import LoginPage
from Utilities.TestStatus import TestStatus
import pytest
import unittest


@pytest.mark.usefixtures("oneSetUp", "setUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)  # RUNS automatically in the class so lp can be used
    def classSetUp(self, oneSetUp):  # onesetup is used to return attr driver or error: 'TestLogin' object has no attribute 'driver'
        self.lp = LoginPage(self.driver)  # video 166 4:20 / self.driver is returned from request.cls.driver = driver(https://gist.github.com/highsmallxu/7ab383bee1bf1f375a66dc8d85ee403c) / beacuse loginpage (__init__ wants driver)
        # self.lp so it is available for the whole class
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_A(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginTitle()
        self.ts.mark(result, "of Get title")  # assert result == True
        result1 = self.lp.verifyloginsucc()
        self.ts.markFinal("Test valid login", result1, "of Valid login")  # assert result1 == True

    @pytest.mark.run(order=1)
    def test_B(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        propic = self.lp.verifyloginfail()
        self.ts.mark(propic, "of Invalid login")    # assert propic == True

# s = LoginTest()
# s.test_validlogin()
    #  py.test -s -v Tests\home\login_tests.py
    # py.test -s -v Tests\home\login_tests.py --browser Chrome