import requests
import json
import time
import sqlite3
from tqdm import tqdm
from openpyxl import Workbook
import sys
# 浏览器信息
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "Content-Type": "application/json",
    "Host": "gs.amac.org.cn",
    "Origin": "http://gs.amac.org.cn",
    "Referer": "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
    "X-Requested-With": "XMLHttpRequest"
}

request_params = {}  # 这个是json请求，是直接发送给服务器的，所以需要先序列化， 使用通用型的web传输的惯用序列化标准，json来序列化


# 遍历获取每一页要post到服务器的参数
def get_post_params(page):
    post_params = {
        'rand': '0.034480063759529056',
        'page': page,
        'size': '20'
    }  # 这些请求参数如果出现在地址栏中， 那么需要使用urlencode方法将这些参数编码
    return post_params


# 获取每页的关键信息,并添加到excel中
def iter_list_values(post_params):
    response = requests.post('http://gs.amac.org.cn/amac-infodisc/api/pof/manager?', params=post_params,
                             data=json.dumps(request_params), headers=headers)  # json 请求, params 是请求参数，data是json请求
    for i in range(20):
        list_values = [json.loads(response.text)['content'][i][x] for x in
                       'managerName fundScale fundCount officeAddress officeProvince primaryInvestType'.split()]
        yield list_values

# 写入数据库
def create_table():
    global creat_table_sql, i, post_params, iter_list_val
    with db_connection:
        creat_table_sql = """CREATE TABLE IF NOT EXISTS %s (公司名称 TEXT, 管理规模 FLOAT, 产品数量 INT, 办公地址 TEXT, 省份 TEXT, 牌照类型 TEXT)""" % table_time_str
        db_connection.execute(creat_table_sql)
        # iter_list_val = iter_list_values(post_params=get_post_params(pages)) # 获取每页的条目的迭代器
        for i in tqdm(range(pages)):  # 获取所有1211页的条目
            post_params = get_post_params(i)
            iter_list_val = iter_list_values(post_params)
            db_connection.executemany("INSERT INTO %s VALUES(?,?,?,?,?,?)" % table_time_str, iter_list_val)
            # count = db_connection.execute('SELECT count(*) FROM %s' % table_time_str).fetchall()[0][0]
            # print('本次获取到%s条记录'%count)


def export_to_excel():
    global run_click
    export_excel = '日期' + str(run_click)
    db_connection = sqlite3.connect('./simu2.db')
    table_names = db_connection.execute(
        """SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name""").fetchall()
    try:
        table_names_list = [x[0] for x in table_names]  # 如果列表不报超出下标的错误
    except:
        print('数据库无任何表！')
    else:
        if export_excel in table_names_list:
            wb = Workbook()
            sheet = wb.active
            sheet.column_dimensions['A'].width = 50
            sheet.column_dimensions['B'].width = 12
            sheet.column_dimensions['C'].width = 9
            sheet.column_dimensions['D'].width = 70
            sheet.column_dimensions['E'].width = 8
            sheet.column_dimensions['F'].width = 30
            table_head = ['公司名称', '管理规模', '产品数量', '办公地址', '省份', '牌照类型']
            sheet.append(table_head)
            data = db_connection.execute('SELECT * FROM %s' % export_excel)
            print('正在导出excel，请稍后...')
            for i in tqdm(data):
                sheet.append(i)
            wb.save(export_excel + '.xlsx')
            print('导出完毕，文件命名为“%s.xlsx”'%export_excel)
        else:
            print('不存在名为“%s”的表！可导出的表有：%s' % (export_excel, table_names_list))


# 主函数
if __name__ == '__main__':
    run_click = input('开始抓取最新数据请直接按回车。如需导出某天的数据，请输入日期（例如：20181105）并按回车：')

    t_start = time.clock()

    if run_click:
        export_to_excel()
    else:
        pages = 1211
        table_time_str = "日期"+time.strftime("%Y%m%d", time.localtime(time.time()))
        db_connection = sqlite3.connect('./simu2.db')
        table_names = db_connection.execute("""SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name""").fetchall() # 返回元素为一个元素为元组的列表
        try:
            table_names_list = [x[0] for x in table_names ] #如果列表不报超出下标的错误
        except: #如果报错，那么说明从未创建过表，则开始创建数据库表
            print('创建数据库表...')
            create_table()
        else: #否则说明不报超出下标的错误，既数据库里有数据表，还需要判断今天的表是否存在过
            if table_time_str not in table_names_list:
                create_table()
            else:
                print('数据库中表名为“%s”的表已存在！'%table_time_str)
                re_run_programs = input('如需覆盖今天所生成表，请输入yes并按回车:')
                if re_run_programs =='yes':
                    db_connection.execute('drop TABLE %s'%table_time_str)
                    db_connection.commit()
                    create_table()
    t_end = time.clock()
    t =int(t_end-t_start)
    print('任务完成，耗时%s秒...'%t)
    quit_program = input('按回车键退出程序...')
    if quit_program == "":
        sys.exit()



