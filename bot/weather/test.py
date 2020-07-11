import csv
import requests
import urllib.request
from  bs4 import BeautifulSoup

city_code_list={ #縣市ID清單
    "基隆":"10017", "臺北":"63", "新北":"65", "桃園":"68", "新竹":"10018", "苗栗":"10005", "臺中":"66", "南投":"10008", "彰化":"10007", "雲林":"10009", "嘉義":"10020", "台南":"67", "高雄":"64", "屏東":"10013", "台東":"10014", "花蓮":"10015", "宜蘭":"10002",
}

temp=[]
city=input("輸入查詢")
#city_code = city_code_list[tmpcounty[UserID]]
city_code = city_code_list[city]
home_page = 'https://www.cwb.gov.tw/V8/C/W/County/County.html?CID='
url = home_page + city_code
print(url)


resp = requests.get(url) #建立爬取對象
soup = BeautifulSoup(resp.text, 'lxml') #建立爬取對象
body= soup.body
data = body.find('div',{'class':'banner_wrap'}) #找到class=banner_wrap的div
ul = data.find('ul')
li = ul.find_all('li')
temp.append(ul)

print(data)