from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sites = {"google.ru": "https:\\www.google.ru",
         "pw.mail.ru": "https:\\pw.mail.ru"}

buttons = {"Новости": "//*[@class='menu_news']",
           "Об игре": "//*[@class='menu_about']",
           "Медиа": "//*[@class='menu_media']",
           "Скачать": "//*[@class='menu_download']",
           "Сообщество": "//*[@class='menu_community']"}

content = {"Новости": "Все новости",
           "Об игре": "Вопросы по крафту",
           "Медиа": "Фан-кит",
           "Скачать": "Системные требования",
           "Сообщество": "Поделки"}

buttons_sc2 = {"ВОЙТИ": "//*[@class='enter']/a[@value='Войти']",
               "Войти": "//*[@class='gmrSignin__actions']/button[@id='js_kit_signin__submit']"}

fields = {"E-mail": "//*[@name='Login']",
          "Пароль": "//*[@name='Password']"}

data = {"Логин": "login",
        "Пароль": "password"}


@when('Зашли на сайт "{text}"')
def step_impl(context, text):
    context.driver.get(sites[text])


@step("Убедились, что появилось поисковое поле")
def step_impl(context):
    assert context.driver.find_element_by_name("q")


@then('Ввели в поисковое поле "{text}"')
def step_impl(context, text):
    search_line = context.driver.find_element_by_name("q")
    search_line.send_keys(text)


@step('Нажали кнопку "Поиск в Google"')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@class='FPdoLc VlcLAe']/center/input[@class='gNO89b']").click()


@then('Нажали на ссылку "{text}"')
def step_impl(context, text):
    context.driver.find_element_by_partial_link_text(text).click()
    window_after = context.driver.window_handles[1]
    context.driver.switch_to_window(window_after)


@then('Нажали на пункт "{text}"')
def step_impl(context, text):
    WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.XPATH, buttons[text])))
    context.driver.find_element_by_xpath(buttons[text]).click()


@step('Убедились, что перешли в раздел "{text}"')
def step_impl(context, text):
    assert content[text] in context.driver.page_source


@step('Нажали кнопку "{text}"')
def step_impl(context, text):
    context.driver.find_element_by_xpath(buttons_sc2[text]).click()


@then('Нашли поле "{text}" и ввели "{text1}"')
def step_impl(context, text, text1):
    WebDriverWait(context.driver, 3).until((EC.presence_of_element_located((By.XPATH, fields[text]))))
    context.driver.find_element_by_xpath(fields[text]).send_keys(data[text1])

@then('Нажали на кнопку "Пополнить счет"')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='bill_link hv']")))
    context.driver.find_element_by_xpath("//*[@class='bill_link hv']").click()
    context.driver.switch_to.frame(context.driver.find_element_by_id('payment_iframe'))
    WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='xform-bonus']")))


@then('Выбрали в выпадающем списке пункт со значением "{text}"')
def step_impl(context, text):
    Select(context.driver.find_element_by_xpath('//*[@id="xform-bonus"]')).select_by_value(text)


@step('Убедились, что значение в поле "Сумма платежа" равно "{text}"')
def step_impl(context, text):
    WebDriverWait(context.driver, 1).until(EC.text_to_be_present_in_element_value((By.ID, "xform-sum"), text))
    assert text in context.driver.find_element_by_id("xform-sum").get_attribute('value')

