import allure
import pytest

from data import FaqData


@allure.feature("Главная страница")
@allure.story("Вопросы о важном")
class TestFaq:

    @allure.title("При нажатии на вопрос №{index} открывается соответствующий ответ")
    @pytest.mark.parametrize("index", range(len(FaqData.ANSWERS)))
    def test_faq_question_opens_answer(self, main_page, index):
        assert main_page.get_faq_answer(index) == FaqData.ANSWERS[index]
