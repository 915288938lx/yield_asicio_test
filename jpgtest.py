link = 'http://i1.1100lu.xyz/1100/vod/201805/14/vod/zgqiowqtyxl.jpg'
import requests
headers= {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"__cfduid=debea90104586a125edc68032ecd037431532138348; Hm_lvt_4ab4576ab990d89616b2b6dc90c03dc1=1532138353,1532138658; Hm_lpvt_4ab4576ab990d89616b2b6dc90c03dc1=1532138658",
"Host":"6666av.vip",
"If-Modified-Since":"Fri, 13 Jul 2018 14:34:51 GMT",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
}
imge_response = requests.get(link,stream=True,allow_redirects=True)
imge_content=imge_response.content
with open('b.jpg','wb') as f:
    f.write(imge_content)