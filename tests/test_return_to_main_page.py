import allure
from pages.page_object_create_order_methods import OrderKickscooter
from pages.qa_scooter_main_page import OrderMainPage


@allure.story('tests')
class TestReturnToMainPage:
    @allure.title('test main page links')
    def test_return_to_main_page_by_samokat_logo(self, driver):
        """
        Тест проверяет: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        order_scooter_main_page.click_on_order_button_header()#кликаем на кнопку заказать сверху
        order_scooter.click_samokat_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_redirection_to_yandex_main_page(self, driver):
        """
        Тест проверяет: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        order_scooter_main_page.get_current_window_handle()
        order_scooter.click_yandex_logo()
        order_scooter.switch_to_new_window(OrderKickscooter.yandex_logo_new)
        assert "https://dzen.ru/?yredirect=true" in driver.current_url
