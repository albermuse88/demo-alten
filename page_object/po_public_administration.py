from selenium.webdriver.common.by import By

from page_object.po_base import BasePage


class PublicAdministrationPage(BasePage):

    def verify_text(self, expected_text):
        expected_text_locator = (By.XPATH, f"//h3[text()='{expected_text}']")
        self.move_element(expected_text_locator)
        self.verify_text_present(expected_text_locator, expected_text)
