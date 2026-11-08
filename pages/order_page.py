import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить форму «Для кого самокат» и нажать «Далее»")
    def fill_customer_form(self, order):
        self.type_text(OrderPageLocators.NAME_INPUT, order["name"])
        self.type_text(OrderPageLocators.SURNAME_INPUT, order["surname"])
        self.type_text(OrderPageLocators.ADDRESS_INPUT, order["address"])
        self.type_text(OrderPageLocators.METRO_INPUT, order["metro"])
        self.click(OrderPageLocators.metro_option(order["metro"]))
        self.type_text(OrderPageLocators.PHONE_INPUT, order["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму «Про аренду» и подтвердить заказ")
    def fill_rent_form(self, order):
        self.type_text(OrderPageLocators.DATE_INPUT, order["date"])
        self.click(OrderPageLocators.FORM_HEADER)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rental_period_option(order["rental_period"]))
        self.click(OrderPageLocators.color_checkbox(order["color"]))
        self.type_text(OrderPageLocators.COMMENT_INPUT, order["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def make_order(self, order):
        self.fill_customer_form(order)
        self.fill_rent_form(order)

    @allure.step("Дождаться окна успешного заказа и получить его заголовок")
    def get_modal_header_text(self):
        self.find_element(OrderPageLocators.STATUS_BUTTON)
        return self.get_text(OrderPageLocators.MODAL_HEADER)

    @allure.step("Нажать «Посмотреть статус»")
    def click_view_status(self):
        self.click(OrderPageLocators.STATUS_BUTTON)
