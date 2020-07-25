from selenium import webdriver

city_code_list={ #縣市ID清單
    "基隆":"10017", "台北":"63", "新北":"65", "桃園":"68", "新竹":"10018", "苗栗":"10005", "台中":"66", "南投":"10008", "彰化":"10007", "雲林":"10009", "嘉義":"10020", "台南":"67", "高雄":"64", "屏東":"10013", "台東":"10014", "花蓮":"10015", "宜蘭":"10002",
}

temp=[]
#city=input("輸入查詢")
city_code = city_code_list[db.getCOUNTY([UserID])]
city_code = city_code_list[city]
home_page = 'https://www.cwb.gov.tw/V8/C/W/County/County.html?CID='
url = home_page + city_code
print(url)

#driver_path = r"D:\\chromedriver.exe"   #存放chromeriver.exe的路徑(版本號要相符)
driver = webdriver.Chrome()
driver.get(url) #啟動Chrome

data = driver.find_element_by_xpath('/html/body/div/div/div/ul').text
text = driver.find_element_by_xpath('/html/body/div/div/div/div/a').text
print(data)
print(text)


file = open('weather.csv', 'w') #開新weather.csv 建立新檔，若有資料則覆蓋
file.write(text+'\n')
file.write(data)
