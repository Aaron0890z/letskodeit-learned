from selenium.webdriver.common.by import By
import time
from Base.Selenium_driver import SeleniumDriver
from Base.BasePage import BasePage
from Utilities.GenericLogger import CustomLogger
import logging


class LoginPage(BasePage):

    def __init__(self, driver):             # accepts a value i.e. driver
        super().__init__(driver)
        self.driver = driver

    # Locators                              # not under init
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _pass_field = "password"
    _login_btn = "//input[@value='Login']"
    _account_btn = "a.dynamic-link>span"
    _logout_btn = "a[href='/logout']"
    _logo = "a.navbar-brand.navbar-logo.text-blue"

    def getSomething(self):
        self.getElement(self._login_link, locatorType="xpath")

    def clickLoginLink(self):
        self.elementclick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendkeys(email, self._email_field)

    def enterPass(self, passw):
        self.sendkeys(passw, self._pass_field)

    def clickLoginBtn(self):
        self.elementclick(self._login_btn, locatorType="xpath")

    def verifyloginsucc(self):
        result = self.elementpresent("//button[@id='dropdownMenu1']//img[contains(@src,'profile')]",
                                       locatorType="xpath")
        return result

    def verifyloginfail(self):
        # result = self.waitForElements("//span[contains(text(),'username or password is invalid')]", locatorType="xpath")
        result = self.ExplicitWait("//span[contains(text(),'username or password is invalid')]", locatorType="xpath", timeout=10, pollFrequency=0.5)
        r1 = self.isDisplayed(element=result)
        return r1

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")

    def login(self, email="", passw=""):
        # self.getSomething()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPass(passw)
        self.clickLoginBtn()

    def logout(self):
        # self.elementclick(self._logo, "css")
        self.ExplicitWait(self._account_btn, "css", timeout=10, pollFrequency=1)
        self.elementclick(self._account_btn, "css")
        self.ExplicitWait(self._logout_btn, "css", timeout=10, pollFrequency=1)
        self.elementclick(self._logout_btn, "css")



    # def invalid_login(self):
    #     self.clickLoginLink()
    #     self.clickLoginBtn()
