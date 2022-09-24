import Utilities.GenericLogger as CL
import logging
from Base.Selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):           # can work without SeleniumDriver
    log = CL.CustomLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super().__init__(driver)             # if selenium removed remove super also
        self.resultList = []

    def setresult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(" ### Verification successful + " + resultMessage + " " + str(result))
                else:
                    self.resultList.append("FAIL")
                    self.log.error(" ### Verification unsuccessful + " + resultMessage + str(result))
            else:
                self.resultList.append("FAIL")
                self.log.error(" ### Verification unsuccessful + " + resultMessage + str(result))
        except:
            self.resultList.append("FAIL")
            self.log.error(" ### Exception occurred !!!")

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setresult(result, resultMessage)

    def markFinal(self, testname, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setresult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testname + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testname + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
