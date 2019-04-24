
def get_cookie():
    url = 'https://www.licai.com/api/v1/ad/get?alias=pc_licai_simu'
    cookies_text = """_uab_collina=153356505485843093493272; BIGipServerpool_gs_sm_nginx=1695197376.20480.0000; _gat=1; __utmt=1; Hm_lvt_2e0ae38a699bc0db3f8f784ca1e310c7=1537618642,1537718832,1537721534,1537762279; Hm_lpvt_2e0ae38a699bc0db3f8f784ca1e310c7=1537762331; Hm_lvt_4f5f61d55230ff308da1069fd4da34dd=1537618642,1537718832,1537721534,1537762280; Hm_lpvt_4f5f61d55230ff308da1069fd4da34dd=1537762331; sessionid=cy91obcrk4um63n509lf9sa4y3xylqkm; TS0149003d=014c43903aee080c0f38a233df30d275a733e6d7d4a7ae897737b5cafc6467fe8b9c896d0fcd52abec3153ec0a843054c738672e239c479dc9159d435623dab1fc5c7175bf; __utma=119783701.496111003.1533565056.1537721534.1537762279.18; __utmb=119783701.5.10.1537762279; __utmc=119783701; __utmz=119783701.1533565056.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.496111003.1533565056; Hm_lvt_c09b6af925ee0121f9617c3f09d2a088=1537618642,1537718831,1537721534,1537762279; Hm_lpvt_c09b6af925ee0121f9617c3f09d2a088=1537762337"""
    li = cookies_text.split(';')
    # print(li)
    for kv in li:
        print(kv)
        aaa = kv.split('=')
        print(aaa   )
        


get_cookie()