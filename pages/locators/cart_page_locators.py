from selenium.webdriver.common.by import By


item_in_cart = (By.CSS_SELECTOR, "div[data-test-id='product-title'] > a")
delete_item_button = (By.CSS_SELECTOR, "div[data-test-id='product-item-delete-btn']")
your_cart_is_empty = (By.CSS_SELECTOR, "div[data-test-id='basket-empty-title']")
