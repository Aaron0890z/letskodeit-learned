from Base.BasePage import BasePage
from selenium.webdriver.support.select import Select


class CoursePage(BasePage):
    def __init__(self, driver):
        super(CoursePage, self).__init__(driver)
        self.driver = driver

    _all_courses = "//a[@href='/courses']"
    _course_dropD = "select[name='categories']"
    _search_box = "//input[@id='search']"
    _search_button = "//button[@type='submit']"
    _JS_course = "//a[@href='/courses/javascript-for-beginners']"
    _course_input = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _JS_course_click = '//div[@data-uniqid="1577353494890"]//a[@href="/courses/javascript-for-beginners"]'
    _JS_enroll = "button.btn-enroll"
    _pay_con = "//h3[contains(text(), 'Payment Information')]"
    _card_no = "//input[@name='cardnumber']"
    _card_exp = "exp-date"
    _card_cvv = "cvc"
    _country_dropD = '//select[@name="country-list"]'
    _button = "//div[@class='col-xs-12']/button"
    _error_message = '//li[@class="card-no cvc expiry text-danger"]//span'
    _CCno_error = "li.card-no.text-danger"
    _CCexpiry_error = "li.expiry.text-danger"
    _CCccv_error = "li.cvc.text-danger"

    def clickAllCourses(self):
        self.elementclick(self._all_courses, "xpath")

    def SearchCourse(self, courseName):
        self.sendkeys(courseName, self._search_box, "xpath")
        self.util.sleep(2)
        self.elementclick(self._search_button, "xpath")

    def selectDropdown(self, value, locator, locatorType, type):
        self.getDropDown(value, locator, locatorType, type)

    def fullCourseName(self, fullCourseName):
        self.mouseHover(self._course_input.format(fullCourseName), "xpath")
        self.util.sleep(2)
        self.elementclick(self._course_input.format(fullCourseName), "xpath")

    def enrollCourse(self):
        self.elementclick(self._JS_enroll, "css")

    def selectingCourse(self, data):
        self.clickAllCourses()
        # self.selectDropdown("Software Development", self._course_dropD, "css", "visible text")

        self.SearchCourse(data)
        # ag = self.getElement(self._JS_course_click, "xpath")
        # self.actions.click(on_element=ag)                     using actionschains
        # self.mouseHover(self._course_input, "xpath")
        # self.util.sleep(2)
        self.fullCourseName(data)
        self.enrollCourse()

    def verifyCoursePresent(self):
        self.clickAllCourses()
        r1 = self.isDisplayed(self._JS_course, "xpath")
        return r1

    def scrollDown(self):
        self.scrollTo(self._pay_con, "xpath")

    def SwitchingFrames(self, value, type):
        self.switchToIframe(value, type)
        # self.driver.switch_to.frame(0)   # "__privateStripeFrame3986"
        # a = self.isDisplayed("//input[@name='cardnumber']", "xpath")
        # self.log.info(str(a))
        # b = self.getElement("//input[@name='cardnumber']", "xpath")
        # return b

    def enterCardNo(self, num):
        self.SwitchingFrames(0, "num")
        self.sendkeys(num, self._card_no, "xpath")
        self.util.sleep(2)
        self.switchToDefaultFrame()

    def enterCardExp(self, date):
        self.SwitchingFrames(1, "num")
        self.sendkeys(date, self._card_exp, "name")
        self.util.sleep(2)
        self.switchToDefaultFrame()

    def enterCardCVV(self, cvv):
        self.SwitchingFrames(2, "num")
        self.sendkeys(cvv, self._card_cvv, "name")
        self.util.sleep(2)
        self.switchToDefaultFrame()

    def clickBuy(self):
        b = self.isEnabled(self._button, "xpath")
        self.log.info(str(b))
        self.elementclick(self._button, "xpath")

    def checkError(self):
        # errorMsg = self.isDisplayed(self._error_message, "xpath")
        # return errorMsg
        cardError = self.isDisplayed(self._CCno_error, "css")  # if card no, cvv, expiry error then show error
        return cardError

    def paymetPage(self, num, date, cvv):
        self.scrollDown()
        # self.firstFrame()
        self.enterCardNo(num)
        self.enterCardExp(date)
        self.enterCardCVV(cvv)
        self.selectDropdown("India", self._country_dropD, "xpath", "visible text")
        self.util.sleep(2)
        self.clickBuy()

    def coursesCheck(self, courseName, num="", date="", cvv=""):
        self.selectingCourse(courseName)
        self.paymetPage(num, date, cvv)
