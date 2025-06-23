
import allure
from Base.base_page import BasePage
from Config.links import links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ProfilePage(BasePage):

    PAGE_URL = links.PROFILE_PAGE
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        with allure.step(f'Change name on {new_name}'):

            first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name.send_keys(Keys.CONTROL, 'a')
            first_name.send_keys(new_name)
            self.name = new_name

    @allure.step('save changes')
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes are saved successfully ')
    def are_changes_saved(self):
        self.wait.until(EC.invisibility_of_element(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))

