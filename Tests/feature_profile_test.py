import random
import allure
import pytest
from Base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_button()
        self.profile_page.is_opened()
        self.profile_page.change_name(f"Test {random.randint(1, 100)}")
        self.profile_page.save_changes()
        self.profile_page.are_changes_saved()
        self.profile_page.make_screenshot("Success")