from DrissionPage import ChromiumPage
import requests,json,pandas
ky_url =  'https://api.kaoyan.cn/pc/school/schoolList'
headers = {
            "referer": "https://www.kaoyan.cn/",
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
             
            '''cuid=f9c9cf78-5ec2-a4f9-9ac6-11fc44a5d718; token_type=access_token; access_token=NWVmNjM1ZjI0OWVmOTVkM2FlMGQ0ZTM3ZDk5YzY2YTg=; refresh_token=NWVmNjM1ZjI0OWVmOTVkM2FlMGQ0ZTM3ZDk5YzY2YTg=; userid=1308534186943971328; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1786966607,1786981982,1787114224,1787123223; Hm_lvt_f184dcac01d7ab6216d471be8e61c26d=1788875048; Hm_lpvt_f184dcac01d7ab6216d471be8e61c26d=1788875048; HMACCOUNT=01D0E9F0FA16BB56'''
}
#{page: 1, size: 20, province_id: "", type: "", feature: "", school_name: "中国石油大学",…}

data = {
    'page': 1,
     'size':20,
    'province_id':"",
    'type':"",
    'feature':"",
    'school_name':""
}
response =requests.post(url=ky_url,headers=headers,data=data)

redata = response.json( )
xxlist = redata['data']['data']
print(redata)
for i in xxlist :
    major_number = i['major_number']
    school_name = i['school_name']
    province_name = i['province_name']
    school_id  = i['school_id']
    print(major_number,school_name,province_name,school_id)
all_data=[]
score_url = 'https://api.kaoyan.cn/pc/school/schoolScore'
data ={
    'school_id':'xid',
    'degree_type':'' ,
    'year':2026
}
response = requests.post(url=score_url,headers=headers,data=data)
redata = response.json( )
print(redata)
for i in redata['data'] :
    data = {
        '学校':i['school_name'],
        '专业':i['name'],
        '代码':i['code'],
        '招生院系':i['depart_name'],
        '总分': i['total'],
        '政治': i['politics'],
        '英语': i['english'],
        '专业课一':i['special_one'],
        '专业课二':i['special_two'],
        '录取年份':i['year'],

    }
    all_data.append(data)
df = pandas.DataFrame(all_data)
df.to_csv('各院校考研数据采集.csv',index=False)













