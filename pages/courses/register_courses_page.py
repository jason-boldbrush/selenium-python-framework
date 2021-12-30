import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@id='search']"
    _search_button = "//*[@id='search']/div/button"
    _course = "//*[@id='course-list']/div/div/a/div[2]/h4"
    _all_courses = "ALL COURSES"
    _fullCourseName = "h4.dynamic-heading:nth-child(1)"
    _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']/div/div/div[2]/div[3]/button"
    _cc_num = "//*[@id='root']/form/span[2]/div/div[2]/span/input[@name='cardnumber']"
    _cc_exp = "//*[@name='exp-date']"
    _cc_cvv = "cvc"
    _submit_enroll = "//form[@id='checkout-form']/div[2]/div[3]/div/div/div[2]/div/button/i"
    _enroll_error_message = "Your card was declined."
    _cc1_iframe = "/html/body/div/form/span[2]/div/div[2]/span/input"
    _course_title = "/html/body/div[1]/div[2]/div/div/div/div/div[2]/h2"


    def clickAllCoursesLink(self):
        self.elementClick(self._all_courses, locatorType="link")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")
        self.elementClick(self._search_button, locatorType="xpath")
        time.sleep(2)

    # def clickSearchButton(self):
    #     self.elementClick(self._search_button, locatorType="xpath")

    # def searchCourse(self):
    #     self.enterCourseName(search=self._course)
    #     self.waitForElement(self._course)
    #     self.clickSearchButton()

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
        self.elementClick(self._enroll_button, locatorType="xpath")
        self.webScroll(direction="down")
        time.sleep(2)

    def enterCardNum(self, num):
        time.sleep(15)
        self.switchToFrame(index=1)
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefault()
        time.sleep(10)

    def enterCardExp(self, exp):
        self.switchToFrame(index=3)
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchToDefault()
        time.sleep(10)

    def enterCardCVV(self, cvv):
        self.switchToFrame(index=2)
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")
        self.switchToDefault()
        time.sleep(2)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()
        self.waitForElement(self._enroll_error_message)

    def verifyEnrollFailed(self):
        time.sleep(30)
        result = self.isElementPresent("//p[text()[contains(.,'Your card was declined.')]]", locatorType="xpath")
        return result

    def verifyCourseTitle(self):
        self.webScroll(direction="up")
        result = self.isElementPresent("//h2[contains(text(), 'JavaScript for beginners')]", locatorType="xpath")

        return result