import allure
import pytest

from data import OrderData, Urls
from pages.order_page import OrderPage
from pages.track_page import TrackPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката (кнопка «Заказать»: {order[entry_point]})")
    @pytest.mark.parametrize("order", OrderData.ORDERS, ids=lambda order: order["entry_point"])
    def test_order_scooter_success(self, driver, main_page, order):
        main_page.click_order_button(order["entry_point"])
        order_page = OrderPage(driver)
        order_page.make_order(order)

        assert "Заказ оформлен" in order_page.get_modal_header_text()

        order_page.click_view_status()
        track_page = TrackPage(driver)
        track_page.click_scooter_logo()
        main_page.wait_for_url(Urls.MAIN_PAGE)

        assert main_page.get_current_url() == Urls.MAIN_PAGE

        main_page.click_yandex_logo()
        main_page.wait_for_url(Urls.YANDEX_PAGE)

        assert main_page.get_current_url() == Urls.YANDEX_PAGE
