import asyncio
import json
import json
payload = {}
from aiohttp import ClientSession

headers2 ="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BAIDUID=E96E48075B3013A23D9C8035567B8D44:FG=1; PSTM=1537532300; delPer=0; BIDUPSID=E61BE62B01ECE93D0D601DE33052E232; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=0; H_PS_PSSID=26524_1436_21117_18560_27111
Host: www.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"""



url = 'https://www.baidu.com/'
# url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager?rand=0.04704504868979775&page=0&size=50'
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
async def hello():
    async with ClientSession() as session:
        async with session.post(url) as response:
            response = await response.read()
            print(response.decode('utf-8'))


loop = asyncio.get_event_loop()
tasks = []

loop.run_until_complete(hello())

