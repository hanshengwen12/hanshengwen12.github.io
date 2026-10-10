import csv
from DrissionPage import ChromiumPage
import time
page = ChromiumPage()
page.get('https://www.zbj.com/sem/index?pmcode=137535808&utm_source=bdpz&utm_medium=SEM')
allData = []
kw = '爬虫'
page.ele('xpath://input[@class="j-header-kw"]').input(kw)
page.ele('.btn-search').click()
new_page = page.latest_tab
new_page.ele('xpath://div[@class="tabs"]/a[3]').click()
for p in range(1,3):
    time.sleep(5)
    items =new_page.eles('.card-item-single')
    for item in items:
        title =item.ele('.task-names').text
        price = item.ele('.total-money').text
        classify = item.ele('.depict-refer').text
        content = item.ele('.contents-text').text
        url = item.ele('./a/@href')
    try:
        status = item.ele('.status-box').text
    except:
        status = item.ele('.status-box orange').text

        allData.append([title,price,classify,status,content,url])
        page.quit()
with open('猪八戒.csv','w',newline="",encoding='utf-8') as f:
    cf = csv.writer(f)
    cf.writerow([' 标题','价格','类型','状态','内容','网址'])
    cf.writerows(allData)


















