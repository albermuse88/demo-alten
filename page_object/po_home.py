from selenium.webdriver.common.by import By

from page_object.po_base import BasePage


class HomePage(BasePage):
    btn_denied_cookies = (By.ID, "tarteaucitronAllDenied2")
    link_sectors_section = (By.XPATH, "//ul[@id='menu-header-es-1']//span[text()='Sectores']")
    link_public_administration = (By.XPATH, "//ul[@id='menu-header-es-1']//span[text()='Administración Pública']")
    link_aeronautic = (By.XPATH, "//ul[@id='menu-header-es-1']//span[text()='Aeronáutica']")

    def access_website(self, url):
        self.driver.get(url)
        self.wait_for_element(self.btn_denied_cookies, 10)
        self.click_element(self.btn_denied_cookies)

    def access_main_section_sectors(self):
        self.hover_over_element(self.link_sectors_section)

    def access_section_public_administration(self):
        self.click_element(self.link_public_administration)

    def access_section_aeronautic(self):
        self.click_element(self.link_aeronautic)
