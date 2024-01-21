import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderKickscooter(BasePage):
    #локатор поля Имя
    name_field = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    # локатор поля Фамилия
    surname_field = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    # локатор поля Адрес
    adress_field = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    # локатор поля Dropdawn metro
    metro_station_dropdown = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    # локатор конкретного метро
    metro_station = [By.XPATH, "//div[text()='Черкизовская']"]

    new_phone_number = "79118982345"
    # локатор поля Телефон
    phone_number_filed = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    # локатор кнопки Далее
    proceed_button = [By.XPATH, '//button[text()="Далее"]']

    rental_start_date_field = [By.XPATH,'//input[@placeholder="* Когда привезти самокат"]']
    rental_date = [By.XPATH, "//div[text()='30']"]
    #локатор поля времени аренды самоката
    rental_time_field = [By.XPATH, "//div[text()='* Срок аренды']"]
    #локатор дропдауна выбора срока Сутки
    one_day_time = [By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div[1]"]
    #локатор кнопки заказать после введения всех данных
    finish_order_button = [By.XPATH, "//div[3]/button[text()='Заказать']"]

    #локатор кнопки Подтвердить заказ
    confirm_order_button = [By.XPATH, '//button[text()="Да"]']
    #локатор кнопки Посмотреть статус
    check_status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    #локатор лого "Самокат"
    samokat_logo = [By.XPATH, '//img[@alt="Scooter"]']

    #локатор лого "Яндекс"
    yandex_logo = [By.XPATH, '//img[@alt="Yandex"]']

    yandex_logo_new = [By.XPATH, "//*[@id='dzen-header']/div[1]/a[1]"]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Enter the name")
    def set_name(self, name):
        enter_name = self.find_element_located(self.name_field)
        enter_name.click()
        enter_name.send_keys(name)
        return enter_name

    @allure.step("Enter the surname")
    def set_surname(self, surname):
        enter_surname = self.find_element_located(self.surname_field)
        enter_surname.click()
        enter_surname.send_keys(surname)
        return enter_surname


    @allure.step("Enter the adress")
    def set_adress(self, adress):
        enter_adress = self.find_element_located(self.adress_field)
        enter_adress.click()
        enter_adress.send_keys(adress)
        return enter_adress
    @allure.step("Enter the metro station")
    def set_metro_station(self):
        self.find_element_located(self.metro_station_dropdown).click()
        metro = self.find_element_located(self.metro_station).click()
        return metro

    @allure.step("Enter the phone number")
    def set_phone_number(self):
        phone = self.find_element_located(self.phone_number_filed).send_keys(self.new_phone_number)
        return phone

    @allure.step("Click proceed button")
    def click_proceed_button(self):
        self.find_element_located(self.proceed_button).click()


    @allure.step("Chose start rental date")
    def set_rental_start_date(self):
        self.find_element_located(self.rental_start_date_field).click()
        self.find_element_located(self.rental_date).click() #выбираем 30 января

    @allure.step("Set rental time")
    def set_rental_time(self):
        self.find_element_located(self.rental_time_field).click()
        self.find_element_located(self.one_day_time).click()

    @allure.step("Click finish order")
    def click_finish_order_button(self):
        self.find_element_located(self.finish_order_button).click()

    @allure.step("Click confirm order")
    def click_confirm_order_button(self):
        self.find_element_located(self.confirm_order_button).click()


    @allure.step("Click check status")
    def click_check_status_button(self):
        self.find_element_located(self.check_status_button).click()

    @allure.step("Click Samokat logo")
    def click_samokat_logo(self):
        self.find_element_located(self.samokat_logo).click()


    @allure.step("Click Yandex logo")
    def click_yandex_logo(self):
        self.find_element_located(self.yandex_logo).click()

