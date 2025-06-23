import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)


    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)


    def is_opened(self):
        with allure.step(f'Open {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body = self.driver.get_screenshot_as_png(),
            name = screenshot_name,
            attachment_type=AttachmentType.PNG
        )

