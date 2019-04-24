from selenium import webdriver
import time
licai = 'https://www.licai.com/simu/company/'
xiehui ='http://gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html'
paipai = 'https://www.simuwang.com'
taobao = 'https://www.taobao.com/'
browser=webdriver.Chrome()
# browser.maximize_window() # 窗口最大化

# browser.add_cookie({'name':'18521315230','value':'0123456a'})


browser.get(licai) # 在当前浏览器中访问百度
browser.find_element_by_xpath('//*[@id="login_window"]/div[2]/div/div[2]/div[2]/span[2]').click()
browser.find_element_by_xpath("//input[@type='text' and @placeholder='手机号']").clear()
browser.find_element_by_xpath("//input[@type='text' and @placeholder='手机号']").send_keys('18521315230')


browser.find_element_by_xpath('//*[@id="q"]').send_keys('电风扇')
search_click = browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[8]/a').click()
jsnext = """document.find_element('class','item next').click()"""
browser.execute_script(jsnext)
title = browser.execute_script('document.title')
print(title)
browser.execute_script("trigger_auth_form('open','login');")




elm = """document.find_element('link text','登录').click();"""
browser.execute_script(elm)

js = """document.find_element_by_xpath('//*[@id="topAll"]/div/div[2]/a[1]').click();"""
# browser.find_element_by_id('login_window').style.display = 'none'
browser.execute_script(js)

time.sleep(6)
browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/button/span').click()
# 新开一个窗口，通过执行js来新开一个窗口
js='window.open("https://blog.csdn.net/DongGeGe214/article/details/52169761");'
browser.execute_script(js)

print (browser.current_window_handle) # 输出当前窗口句柄（百度）
handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
print (handles)  # 输出句柄集合

for handle in handles:# 切换窗口（切换到搜狗）
    if handle!=browser.current_window_handle:
        print ('switch to ',handle)
        browser.switch_to.window(handle)
        print (browser.current_window_handle)  # 输出当前窗口句柄（搜狗）
        break


# browser.close() #关闭当前窗口（搜狗）
browser.switch_to.window(handles[1]) #切换回百度窗口
print(browser.title)
# print(browser.page_source)
import time
time.sleep(4)
browser.quit()

a = b'\xe9'
print(type(a))
a.decode('cp1252')
print(a)

open('cafe.txt','w',encoding='utf-8').write('café')
print(open('cafe.txt').read())



keys = ('a','b','c')
values = ('haode','no','thanks')

dic = {key:value for key in keys for value in values}
print(dic)
print(dic.get('w','ong'))


from collections import OrderedDict
with open('dd.txt') as fp:
    lines = fp.readlines()

    # print(lines)

enu = enumerate(lines,1)
# print(list(enu))
orderd = OrderedDict(enu)

for k,v  in orderd.items():
    print(k,v)
a = list
dic = {str(key):str.strip(value) for key, value in enumerate(lines,1)}
# print(dic)


import collections
from collections import Counter
li = 'asdfasdtadfbvcxzhujtyjhchnvuioyuewrwafdsgvstwatdsgvfxdhs'
ct = Counter(li)
ct
defautdict = collections.defaultdict(list)
defautdict['w'].append('a')
print(defautdict.get('s'))