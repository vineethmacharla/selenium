import time

import driver as driver
from selenium import webdriver


driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://www.cricbuzz.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='teamDropDown']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='page-wrapper']/div[5]/div[1]/div[2]/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='page-wrapper']/span[2]/span/div[2]/nav/a[3]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='series-matches']/div[3]/div/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='matchCenter']/div[3]/div[2]/div[2]")
time.sleep(2)
x=driver.find_element_by_xpath("//*[@id='matchCenter']/div[3]/div[2]/div[2]").text
print(x)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='matchCenter']/div[2]/nav/a[2]").click()
time.sleep(2)
players = driver.find_elements_by_xpath("//*[@class='cb-col cb-col-100 cb-scrd-itms']")
players = players[:10]
y = []
for i in players:
    # print(i.text)
    y.append(i.text)
    # print('----------------------------')
for i in y:
    i = i.split('\n')
    if i[0].find('Thakur') >= 0:
        print('{} Score is {}'.format(i[0], i[2]))