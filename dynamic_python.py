from selenium import webdriver
import time

br = webdriver.Chrome()
br.get('https://www.licai.com')
print('you can logn in now ....')

print('you have 10 seconds to log in ')
time.sleep(20)
br.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/ul/li[3]/a').click()
# print(br.page_source)