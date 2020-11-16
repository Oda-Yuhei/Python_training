from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time

#--------------[ドライバーの指定/h]---------------------
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.e-typing.ne.jp/roma/variety/long.asp")
#--------------[ドライバーの指定/r]---------------------
time.sleep(1)

element = driver.find_element_by_partial_link_text("オリジナル")
element.click()

time.sleep(1)

iframe = driver.find_element_by_id('typing_content')
driver.switch_to_frame(iframe)

element = driver.find_element_by_id('start_btn')
element.click()

time.sleep(1)
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.SPACE)

time.sleep(4)
inputText = driver.find_element_by_css_selector('#sentenceText').find_elements_by_css_selector('span')[1].text

for sendText in inputText:
  driver.find_element_by_tag_name('body').send_keys(sendText)
  time.sleep(0.01)

