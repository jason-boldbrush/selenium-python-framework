from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4388 2222 3333 4444", 1220, "123"), ("Learn Python 3 from scratch", "4388 2223 3334 4445", "1224", "234" ))
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.clickAllCoursesLink()
        self.courses.searchCourse()
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result1, "Payment Declined - Test Successful")
        result2 = self.courses.verifyCourseTitle()
        self.ts.mark(result2, "Course Title Verified")











