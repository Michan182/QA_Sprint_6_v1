from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropDownQuestions(BasePage):
    # локатор вопроса сколько стоит
    how_much = [By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"]
    # локатор ответа на вопрос сколько стоит
    how_much_answer = [By.XPATH, "//div[@id='accordion__panel-0']/p"]

    # локатор вопроса сколько самокатов можно заказать
    how_much_scooters = [By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    # локатор ответа на вопрос сколько самокатов можно заказать
    how_much_scooters_answer = [By.XPATH, "//div[@id='accordion__panel-1']/p"]

    # локатор вопроса сколько время аренды
    how_much_time = [By.XPATH, "//div[text()='Как рассчитывается время аренды?']"]
    # локатор ответа на вопрос сколько время аренды
    how_much_time_answer = [By.XPATH, "//div[@id='accordion__panel-2']/p"]

    # локатор вопроса сколько заказ сегодня
    order_today = [By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    # локатор ответа на вопрос заказ сегодня
    order_today_answer = [By.XPATH, "//div[@id='accordion__panel-3']/p"]

    # локатор вопроса можно ли продлить заказ
    order_extend_time = [By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    # локатор ответа на вопрос можно ли продлить заказ
    order_extend_time_answer = [By.XPATH, "//div[@id='accordion__panel-4']/p"]

    # локатор вопроса привозите ли зарядку
    charger_delivery = [By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    # локатор ответа на вопрос привозите ли зарядку
    charger_delivery_answer = [By.XPATH, "//div[@id='accordion__panel-5']/p"]

    # локатор вопроса можно ли отменить заказ
    cancel_order = [By.XPATH, "//div[text()='Можно ли отменить заказ?']"]
    # локатор ответа на вопрос можно ли отменить заказ
    cancel_order_answer = [By.XPATH, "//div[@id='accordion__panel-6']/p"]

    # локатор вопроса можно ли привезти за МКАД
    far_delivery = [By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']"]
    # локатор ответа на вопрос можно ли привезти за МКАД
    far_delivery_answer = [By.XPATH, "//div[@id='accordion__panel-7']/p"]

    # метод инициализации класса
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # метод получения текста из элемента
    def get_text_from_element(self, locator):
        element = self.find_element_located(locator)
        text = element.get_attribute('textContent')
        return text

