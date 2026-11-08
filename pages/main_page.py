import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу и принять куки")
    def open_main_page(self):
        self.open(Urls.MAIN_PAGE)
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать на вопрос №{index} и получить текст ответа")
    def get_faq_answer(self, index):
        self.click(MainPageLocators.faq_question(index))
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step("Нажать кнопку «Заказать» ({entry_point})")
    def click_order_button(self, entry_point):
        self.click(MainPageLocators.ORDER_BUTTONS[entry_point])
