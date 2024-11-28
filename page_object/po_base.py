import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        logging.info(f"Elemento esperado encontrado: {locator}")
        return element

    def click_element(self, locator):
        self.wait_for_element(locator).click()
        logging.info(f"Elemento clicado: {locator}")

    def find_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        logging.info(f"Elemento encontrado: {locator}")
        return element

    def scroll_into_view(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.info(f"Elemento movido en la pantalla: {locator}")

    def move_element(self, element):
        source_element = self.wait_for_element(element)
        actions = ActionChains(self.driver)
        actions.move_to_element(source_element).perform()
        logging.info(f"Performing a move action to element: {element}")
        # actions.click_and_hold(source_element).move_by_offset(x_offset, y_offset).release().perform()


    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        logging.info(f"Cursor movido sobre el elemento: {locator}")

    def verify_text_present(self, locator, expected_text, timeout=10):
        try:
            element = self.wait_for_element(locator, timeout)
            actual_text = element.text
            assert actual_text == expected_text, f"Error en el texto: se esperaba '{expected_text}', pero se recibió '{actual_text}'"
            logging.info(f"Texto verificado correctamente en el elemento: {locator}")
        except AssertionError as e:
            logging.error(f"Assertion Failed: {e}")
            raise
        except Exception as e:
            logging.error(f"Error al verificar el texto: {e}")
            raise

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)
        logging.info(f"Captura de pantalla guardada en: {file_path}")
