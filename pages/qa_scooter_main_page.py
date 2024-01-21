from pages.base_page import BasePage
from locators import StartPageScooterLocators


class OrderMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def click_on_order_button_header(self):
        return self.find_element_located_click(StartPageScooterLocators.ORDER_BUTTON_HEADER, time=3)

    def click_on_order_button_footer(self):
        return self.find_element_located_click(StartPageScooterLocators.ORDER_BUTTON_FOOTER,time=3)

