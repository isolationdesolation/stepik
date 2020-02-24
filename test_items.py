import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), \
        "Не найдена кнопка добавления товара в корзину"
