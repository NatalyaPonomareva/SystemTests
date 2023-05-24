import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_user_authorization():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element("xpath",'//*[@id="header_container"]/div[2]/span')
    assert title_text.text == "Products"

def test_add_jacket_to_the_shopcart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск ссылки элемента позиции магазина и клик по ссылке
    item_name = driver.find_element("xpath", '//*[@id="item_5_title_link"]/div')
    item_name.click()

    # Поиск кнопки добавления товара и клик по этой кнопке
    item_add_button = driver.find_element("xpath", '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    item_add_button.click()

    # Поиск кнопки корзины и клик по этой кнопке
    shopping_cart = driver.find_element("xpath", '//*[@id="shopping_cart_container"]/a')
    shopping_cart.click()

    item_description = driver.find_element("xpath", '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[1]')
    item_name = driver.find_element("xpath", '//*[@id="item_5_title_link"]/div')

    assert item_name.text == "Sauce Labs Fleece Jacket"
    assert item_description.text == "It's not every day that you come across a midweight quarter-zip fleece jacket" \
                                   " capable of handling everything from a relaxing day outdoors to a busy day at " \
                                   "the office."


if __name__ == '__main__':
    test_user_authorization();
    test_add_jacket_to_the_shopcart()

