#{dataid} 為各資料集代碼 (參照：資料清單)  ex.F-A0012-001              
#{apikey} 為會員帳號對應之授權碼  ex.CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678
#{format} 為資料格式，請參照各資料集頁面確認可下載之檔案格式  ex.XML、CAP、JSON、ZIP、KMZ、GRIB2
#範例：https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-EB4703E5-E2F4-4CA1-8C04-FB94D6B2F6B8&format=json              
#並請加入快取功能，如上述所示。
#API清單  https://opendata.cwb.gov.tw/dist/opendata-swagger.html

import requests
import json

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-EB4703E5-E2F4-4CA1-8C04-FB94D6B2F6B8&format=json'

res = requests.get(url)
data = json.loads(res.text)

final_list = data["cwbopendata"]["dataset"]["location"]


def weather():
    city_w = []
    for i in final_list:
        if i['locationName'] == '臺北市':
            data = i
            city = data['locationName']
            for j in range(0,3):
                dic = {}
                r = []
                for i in data['weatherElement']:
                    r.append(i['time'][j])            
                l = []
                for i in r:
                    l.append(i['parameter']['parameterName'])
                l.append(f"{i['startTime'][11:16]}"'-'f"{i['endTime'][11:16]}")
                dic[city] = l
                city_w.append(dic)
    return city_w





