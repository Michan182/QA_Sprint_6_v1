import allure
import pytest

from pages.page_object_dropdown import DropDownQuestions

@allure.story('tests')
class TestDropdown:
    @allure.title('test questions')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text",
                             [(DropDownQuestions.how_much, DropDownQuestions.how_much_answer,
                               "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (DropDownQuestions.how_much_scooters, DropDownQuestions.how_much_scooters_answer,
                               "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                               "можете просто сделать несколько заказов — один за другим.")
                              ])
    def test_dropdown_questions(self, driver, question_locator, answer_locator, expected_text):
        """
        Параметризованный тест проверки раскрытия dropdown в разделе "Вопросы" на первые два вопроса:.
        Сколько стоит?
        Сколько можно заказать самокатов?
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(question_locator)
        dropdown.find_element_located(answer_locator)
        element = dropdown.get_text_from_element(answer_locator)
        assert element == expected_text


    def test_dropdown_how_much_time(self, driver):
        """
        Данный тест проверяет раскрытие dropdown на сколько времени можно заказать
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.how_much_time)
        element = dropdown.get_text_from_element(DropDownQuestions.how_much_time_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт " \
                        "времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли " \
                        "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_order_taday(self, driver):
        """
        Данный тест проверяет раскрытие dropdown можно ли заказать сегодня
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.order_today)
        element = dropdown.get_text_from_element(DropDownQuestions.order_today_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_order_extend_time(self, driver):
        """
        Данный тест проверяет раскрытие dropdown продление заказа
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.order_extend_time)
        element = dropdown.get_text_from_element(DropDownQuestions.order_extend_time_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_charger_delivery(self, driver):
        """
        Данный тест проверяет раскрытие dropdown привезти зарядку
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.charger_delivery)
        element = dropdown.get_text_from_element(DropDownQuestions.charger_delivery_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете " \
                        "кататься без передышек и во сне. Зарядка не понадобится."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_cancel_order(self, driver):
        """
        Данный тест проверяет раскрытие dropdown отменить заказ
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.cancel_order)
        element = dropdown.get_text_from_element(DropDownQuestions.cancel_order_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все " \
                        "же свои."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_far_delivery(self, driver):
        """
        Данный тест проверяет раскрытие dropdown привезти за МКАД
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(DropDownQuestions.far_delivery)
        element = dropdown.get_text_from_element(DropDownQuestions.far_delivery_answer)
        text_inside = element
        # ожидаемый текст
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text
