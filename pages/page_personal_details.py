from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderConfirmedLocators:
    LOCATOR_ORDER_CONFIRMED = (By.XPATH, "//div[text()='Заказ оформлен']")
class OrderConfirmed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def get_elements_order_confirmed(self):
        all_elements = self.find_elements_located(OrderConfirmedLocators.LOCATOR_ORDER_CONFIRMED)
        order_confirmed_text = [element.text for element in all_elements]
        return order_confirmed_text
