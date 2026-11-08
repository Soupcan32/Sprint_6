from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[starts-with(@class, 'App_CookieButton')]")

    ORDER_BUTTONS = {
        "top": (By.XPATH, "//div[starts-with(@class, 'Header_Nav')]/button[text()='Заказать']"),
        "bottom": (By.XPATH, "//div[starts-with(@class, 'Home_FinishButton')]/button[text()='Заказать']"),
    }

    @staticmethod
    def faq_question(index):
        return By.XPATH, f"(//div[@class='accordion__button'])[{index + 1}]"

    @staticmethod
    def faq_answer(index):
        return By.XPATH, f"(//div[@class='accordion__panel'])[{index + 1}]"
