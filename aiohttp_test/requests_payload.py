import requests
import json
from openpyxl import Workbook
def get_dict(page):

    post_params = {
    'rand':'0.034480063759529056',
    'page':page,
    'size':'20'
    } # 这些请求参数如果出现在地址栏中， 那么需要使用urlencode方法将这些参数编码
    return post_params
request_params = {}# 这个是json请求，是直接发送给服务器的，所以需要先序列化， 使用通用型的web传输的惯用序列化标准，json来序列化


headers = {
"Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive",
"Content-Length":"2",
"Content-Type":"application/json",
"Host":"gs.amac.org.cn",
"Origin":"http://gs.amac.org.cn",
"Referer":"http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
"X-Requested-With":"XMLHttpRequest"
}





def get_excel(sheet,page,items_num):
    post_params = get_dict(page,items_num)
    response = requests.post('http://gs.amac.org.cn/amac-infodisc/api/pof/manager?',params = post_params,data=json.dumps(request_params),headers=headers) #json 请求, params 是请求参数，data是json请求
    list_values = [json.loads(response.text)['content'][i][x] for x in
                   'managerName fundScale fundCount officeAddress officeProvince primaryInvestType'.split() for i in
                   range(items_num)]
    sheet.append(list_values)

if __name__ == '__main__':
    wb = Workbook()
    sheet = wb.active
    table_head = ['公司名称', '管理规模', '产品数量', '办公地址', '省份', '牌照类型']
    sheet.append(table_head)
    page = 1211
    items_num = 20
    get_excel(sheet,page,items_num)
    wb.save('simu.xlsx')
