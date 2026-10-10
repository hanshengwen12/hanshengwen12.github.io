from DrissionPage import ChromiumPage
import time,csv,jsonpath,json


search = '笔记本电脑'
page = ChromiumPage()
page.listen.start('https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/',method='POST')
time.sleep(1)
page.get(f'https://www.goofish.com/search?spm=a21ybx.home.searchHistory.1.4c053da6Wq28F9&q={search}')
res = page.listen.wait()
resdata = res.response.body
exContent = jsonpath.jsonpath(resdata, '$..exContent')
all_data =[]
for i in exContent:
    try:
        area = i['area']
        price = i['detailParams']['soldPrice']
        title = i['detailParams']['title'][:15]
        all_data.append([area, price, title])
    except Exception as e:
        print(e)
with open(f'闲鱼{search}.csv','w',newline='',encoding='utf-8-sig')as f:
    cf = csv.writer(f)
    cf.writerow(['商品区域','商品价格','商品名称'])
    cf.writerows(all_data)



