from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def TestUserAuthorization():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, \
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
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
    title = driver.find_element("xpath", '//*[@id="header_container"]/div[2]/span')
    assert title.text == "Products"
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def TestEmptyPassword():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, \
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    excepted_url = driver.current_url
    # Действия с формами
    input_username.send_keys("standard_user")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    message = driver.find_element("xpath",'//*[@id="login_button_container"]/ \
                                  div/form/div[3]/h3')
    assert message.text == "Epic sadface: Password is required"
    assert driver.current_url == excepted_url


def TestEmptyUsername():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, \
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    excepted_url = driver.current_url
    # Действия с формами
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    message = driver.find_element("xpath", '//*[@id="login_button_container"]/\
                                  div/form/div[3]/h3')
    assert message.text == "Epic sadface: Username is required"
    assert driver.current_url == excepted_url


def TestAddJacketToTheShopcart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    # Поиск ссылки элемента позиции магазина и клик по ссылке
    item_name = driver.find_element("xpath", '//*[@id="item_5_title_link"]/div')
    item_description = driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                                    div/div[4]/div[2]/div[1]/div')
    expected_item_name = item_name.text
    expected_item_description = item_description.text
    item_name.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=5"

    # Поиск кнопки добавления товара и клик по этой кнопке
    item_add_button = driver.find_element("xpath",'//*[@id="add-to-cart-\
                                          sauce-labs-fleece-jacket"]')
    item_add_button.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=5"

    # Поиск кнопки корзины и клик по этой кнопке
    shopping_cart = driver.find_element("xpath", '//*[@id="shopping_cart_container"]/a')
    shopping_cart.click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    item_description = driver.find_element("xpath", '//*[@id="cart_contents_container"]\
                                           /div/div[1]/div[3]/div[2]/div[1]')
    item_name = driver.find_element("xpath", '//*[@id="item_5_title_link"]/div')

    assert item_name.text == expected_item_name
    assert item_description.text == expected_item_description


def TestCorrectItemsCount():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    expected_item_count = 0
    item_add_button = driver.find_element("xpath", '//*[@id="add-to-cart-test.\
                                          allthethings()-t-shirt-(red)"]')
    item_add_button.click()
    expected_item_count += 1
    item_add_button = driver.find_element("xpath", '//*[@id="add-to-cart-sauce-\
                                          labs-backpack"]')
    item_add_button.click()
    expected_item_count += 1
    item_add_button = driver.find_element("xpath", '//*[@id="add-to-cart-sauce-\
                                          labs-onesie"]')
    item_add_button.click()
    expected_item_count += 1

    item_count = int(driver.find_element("xpath", '//*[@id="shopping_cart_\
                                         container"]/a/span').text)
    assert item_count == expected_item_count


def TestCorrectTotalSum():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    item_add_button = driver.find_element("xpath", '//*[@id=\
                            "add-to-cart-sauce-labs-bike-light"]')
    item_add_button.click()
    expected_total_sum = float(driver.find_element("xpath", '//*[@id=\
      "inventory_container"]/div/div[2]/div[2]/div[2]/div').text.replace('$', ''))
    item_add_button = driver.find_element("xpath", '//*[@id="add-to-cart-test.\
                                          allthethings()-t-shirt-(red)"]')
    item_add_button.click()
    expected_total_sum = expected_total_sum + float(driver.\
                                 find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[6]/div[2]/div[2]/div').text.replace('$', ''))

    shopping_cart = driver.find_element("xpath", '//*[@id="shopping_cart_container"]/a')
    shopping_cart.click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    checkout = driver.find_element("xpath", '//*[@id="checkout"]')
    checkout.click()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    input_first_name = driver.find_element("xpath", '//*[@id="first-name"]')
    input_last_name = driver.find_element("xpath", '//*[@id="last-name"]')
    input_zip = driver.find_element("xpath", '//*[@id="postal-code"]')
    continue_button = driver.find_element("xpath", '//*[@id="continue"]')
    # Действия с формами
    input_first_name.send_keys("Natalya")
    input_last_name.send_keys("Ponomareva")
    input_zip.send_keys("123")
    continue_button.click()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    total_sum = float(driver.find_element("xpath", '//*[@id="checkout_summary_\
        container"]/div/div[2]/div[6]').text.replace('Item total: $', ''))
    assert total_sum == expected_total_sum


def TestNoAccessWithoutAuthorization():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")
    start_url = driver.current_url

    driver.get("https://www.saucedemo.com/inventory.html")
    assert driver.current_url == start_url
    message = driver.find_element("xpath", '//*[@id="login_button_container"]/div/\
                                           form/div[3]/h3')
    assert message.text == "Epic sadface: You can only access '/inventory.html' when\
                                you are logged in."


def TestInvalidPassword():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")
    expected_url = driver.current_url

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("problem_user")
    input_password.send_keys("invalid_password")
    login_button.send_keys(Keys.RETURN)

    assert driver.current_url == expected_url
    message = driver.find_element("xpath", '//*[@id="login_button_container"]/\
                                           div/form/div[3]/h3')
    assert message.text == "Epic sadface: Username and password \
                       do not match any user in this service"


def TestSortingByPriceHiLo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    sort_button = driver.find_element("xpath", '//*[@id="header_container"]/\
                                      div[2]/div/span/select')
    sort_button.click()
    sort_button = driver.find_element("xpath", '//*[@id="header_container"]/\
                                      div[2]/div/span/select/option[4]')
    sort_button.click()
    price_first = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[1]/div[2]/div[2]/div').text.replace('$', ''))
    price_second = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[2]/div[2]/div[2]/div').text.replace('$', ''))
    price_third = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[3]/div[2]/div[2]/div').text.replace('$', ''))
    price_fourth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[4]/div[2]/div[2]/div').text.replace('$', ''))
    price_fifth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[5]/div[2]/div[2]/div').text.replace('$', ''))
    price_sixth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                   div/div[6]/div[2]/div[2]/div').text.replace('$', ''))
    assert price_first >= price_second
    assert price_second >= price_third
    assert price_third >= price_fourth
    assert price_fourth >= price_fifth
    assert price_fifth >= price_sixth

def TestSortingByPriceLoHi():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,\
                              executable_path=r'D:\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("xpath", '//*[@id="user-name"]')
    input_password = driver.find_element("xpath", '//*[@id="password"]')
    login_button = driver.find_element("xpath", '//*[@id="login-button"]')

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    sort_button = driver.find_element("xpath", '//*[@id="header_container"]/\
                                      div[2]/div/span/select')
    sort_button.click()
    sort_button = driver.find_element("xpath", '//*[@id="header_container"]/\
                                      div[2]/div/span/select/option[3]')
    sort_button.click()
    price_first = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[1]/div[2]/div[2]/div').text.replace('$', ''))
    price_second = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[2]/div[2]/div[2]/div').text.replace('$', ''))
    price_third = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[3]/div[2]/div[2]/div').text.replace('$', ''))
    price_fourth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[4]/div[2]/div[2]/div').text.replace('$', ''))
    price_fifth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[5]/div[2]/div[2]/div').text.replace('$', ''))
    price_sixth = float(driver.find_element("xpath", '//*[@id="inventory_container"]/\
                                  div/div[6]/div[2]/div[2]/div').text.replace('$', ''))
    assert price_first <= price_second
    assert price_second <= price_third
    assert price_third <= price_fourth
    assert price_fourth <= price_fifth
    assert price_fifth <= price_sixth


if __name__ == '__main__':
    TestEmptyPassword()
    TestEmptyUsername()
    TestUserAuthorization()
    TestAddJacketToTheShopcart()
    TestCorrectItemsCount()
    TestCorrectTotalSum()
    TestNoAccessWithoutAuthorization()
    TestInvalidPassword()
    TestSortingByPriceHiLo()
    TestSortingByPriceLoHi()
