from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    # --- Ќовые методы дл€ извлечени€ данных ---
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # --- ћетоды проверки теперь принимают аргументы ---
    def should_be_product_added_to_basket(self, product_name):
        message_product_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert product_name == message_product_name, (
            f"Product name in success message does not match: "
            f"expected '{product_name}', got '{message_product_name}'"
        )

    def should_be_basket_total_equal_product_price(self, product_price):
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text
        assert product_price == basket_total, (
            f"Basket total does not match product price: "
            f"expected '{product_price}', got '{basket_total}'"
        )
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"