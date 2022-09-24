import time
from pages.home.login_page import LoginPage
from Utilities.TestStatus import TestStatus
from pages.Courses.Course_Page import CoursePage
import pytest
import unittest
from ddt import ddt, data, unpack
from Utilities.CSVfileReader import CSVReader


@pytest.mark.usefixtures("oneSetUp", "setUp")
@ddt
class TestCourses(unittest.TestCase):

    @pytest.fixture(autouse=True)  # RUNS automatically in the class so lp can be used
    def classSetUp(self, oneSetUp):  # onesetup is used to return attr driver or error: 'TestLogin' object has no attribute 'driver'
        # self.lp = LoginPage(self.driver)  # video 166 4:20 / self.driver is returned from request.cls.driver = driver(https://gist.github.com/highsmallxu/7ab383bee1bf1f375a66dc8d85ee403c) / beacuse loginpage (__init__ wants driver)
        # self.lp so it is available for the whole class
        self.ts = TestStatus(self.driver)
        self.cp = CoursePage(self.driver)

    # @pytest.mark.run(order=1)
    # def test_validlogin(self):
        # self.lp.login("test@email.com", "abcabc")
        # result = self.lp.verifyLoginTitle()
        # self.ts.mark(result, "of Get title")  # assert result == True
        # result1 = self.lp.verifyloginsucc()
        # self.ts.mark(result1, "of Valid login")  # assert result1 == True

    # @pytest.mark.run(order=2)
    # def test_validCourses(self):
    #     r = self.cp.verifyCoursePresent()
    #     self.ts.mark(r, "Course displayed ")

    @pytest.mark.run(order=1)
    @data(*CSVReader("testdata.csv"))   # * informs that there could be multiple arguments
    # @data(("JavaScript for beginners", '9004566578453208', '0625', '8766'), ("Complete Test Automation", '9004566578453208', '0625', '8766'))   # (tuple) / if data provided from here
    @unpack                                                                   # unpack for list and tuples
    def test_C(self, courseName, CCnum, CCexp, CCcvv):
        self.cp.coursesCheck(courseName, CCnum, CCexp, CCcvv)
        r1 = self.cp.checkError()
        self.ts.markFinal("Courses ", r1, "Error message displayed")
        # self.cp.clickAllCourses()
        # r1 = self.cp.verifyCoursePresent()
        # self.ts.markFinal("Checking course ", r1, " JS ")

    # py.test -s -v Tests\Courses\Courses_test.py --browser Chrome