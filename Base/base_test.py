import pytest
from Config.data import Data
from Pages.dashboard_page import DashboardPage
from Pages.login_page import LoginPage
from Pages.profile_page import ProfilePage


class BaseTest:

    data : Data

    login_page: LoginPage
    profile_page: ProfilePage
    dashboard_page: DashboardPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.dashboard_page = DashboardPage(driver)

