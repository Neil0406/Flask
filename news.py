import json
from newsapi import NewsApiClient

# newsapi = NewsApiClient(api_key='')    #API Key

# all_articles = newsapi.get_everything(q='國際 AND NOT 外遇',
#                                       domains='ettoday.net,Technews.tw,Setn.com,udn.com,Ltn.com.tw',
#                                       language='zh',
#                                       sort_by='publishedAt', #由新到舊
#                                       page_size = 30,
#                                       page = 100
#                                       ) #篇幅為100
# fn = 'Exam2-2.json'
# with open(fn,'w',encoding ='utf8') as file:
#     json.dump(all_articles,file,ensure_ascii=False)


# print(all_articles['articles'])

#----------------------以上為原始程式 下面使用存取的json檔測試--------------------------

def news():
    fn = 'Exam2-2.json'

    with open(fn,'r') as file:
        d = json.load(file)

    data = d['articles']
    title = []
    des = []
    url = []
    img = []

    for i in data[:10]:
        title.append(i['title'])
        des.append(i['description'])
        url.append(i['url'])
        img.append(i['urlToImage'])
    mylist = zip(title, des, url, img)
    return mylist

