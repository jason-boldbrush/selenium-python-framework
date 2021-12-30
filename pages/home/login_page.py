import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//*[@id='page']/div[2]/div/div/div/div/form/div[4]/div[1]/input"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("zl-navbar-rhs-img",
                                       locatorType="class")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(), 'Your username or password is invalid. Please try again.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        # logoutLinkElement = self.waitForElement(locator=".zl-navbar-rhs-img", locatorType="css")
        self.elementClick(locator="/html/body/div[1]/div[1]/div/nav/div/div[2]/div[1]/div/div/ul/li[3]/a",
                          locatorType="xpath")
