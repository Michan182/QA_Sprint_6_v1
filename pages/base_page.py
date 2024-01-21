from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').click()

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Elements not found in {locator}')

    def scroll_and_click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'Element not found in {locator}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    # Добавляем метод для получения текущего окна
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_current_url(self):
        return self.driver.get_current_url()

    def find_window(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))

    def switch_to_new_window(self,locator, time=10):
        current_window = self.driver.current_window_handle
        self.find_window()
        all_windows = self.driver.window_handles
        new_window = next(window for window in all_windows if window != current_window)
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                               message=f'Elements not found in {locator}')