from Base.Selenium_driver import SeleniumDriver
from traceback import print_stack
from Utilities.Util import Util


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
        None
        """
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titletoverify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titletoverify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
