from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

buttons = {"Новости": "//*[@id='menu']/li[1]/a",
           "Об игре": "//*[@id='menu']/li[2]/a",
           "Медиа": "//*[@id='menu']/li[3]/a",
           "Скачать": "//*[@id='menu']/li[4]/a",
           "Сообщество": "//*[@id='menu']/li[5]/a"}

content = {"Новости": "Все новости",
           "Об игре": "Вопросы по крафту",
           "Медиа": "Фан-кит",
           "Скачать": "Системные требования",
           "Сообщество": "Поделки"}

@when('Зашли на сайт "google.ru"')
def step_impl(context):
    context.driver.get("https:\\www.google.ru")


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


@when('Зашли на сайт "pw.mail.ru"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Зашли на сайт "pw.mail.ru"')


@step('Нажали кнопку "Войти"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Нажали кнопку "Войти"')


@then('Нашли поле "E-mail"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Нашли поле "E-mail"')


@step("Ввели логин")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Ввели логин')


@then('Нашли поле "Пароль"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Нашли поле "Пароль"')


@step("Ввели пароль")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Ввели пароль')


@then('Выбрали в выпадающем списке пункт со значением ""')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Выбрали в выпадающем списке пункт со значением ""')


@step('Убедились, что значение равно ""')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Убедились, что значение равно ""')


