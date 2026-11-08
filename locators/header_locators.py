from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO = (By.XPATH, "//a[starts-with(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[starts-with(@class, 'Header_LogoYandex')]")
