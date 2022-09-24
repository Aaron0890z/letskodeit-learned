import unittest
from Tests.home.login_tests import TestLogin
from Tests.Courses.Courses_test import TestCourses


# Get all the tests from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCourses)

# Create test suite combining all test classes
smoketest = unittest.TestSuite([tc1, tc2])      # smoketest - can be named regression or etc/ [tc1, tc2] - list of tc

unittest.TextTestRunner(verbosity=2).run(smoketest)

#  py.test Tests\test_suite.py --browser Chrome
