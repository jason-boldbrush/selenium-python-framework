from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.clickAllCoursesLink()
        self.courses.searchCourse()
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse("4388 2222 3333 4444", "04/22", "123")
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Payment Declined - Test Successful")
        result2 = self.courses.verifyCourseTitle()
        self.ts.mark(result2, "Course Title Verified")











