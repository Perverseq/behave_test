from selenium import webdriver
import os





def before_all(context):
    context.driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
