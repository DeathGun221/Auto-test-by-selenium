import allure
from Base.base_page import BasePage
from Config.links import links
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step('Click My info button')
    def click_my_info_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
