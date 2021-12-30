import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _user_settings_icon = ".zl-navbar-rhs-img"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToUserSettingsIcon(self):
        # userSettingElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._user_settings_icon, locatorType="css")

