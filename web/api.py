from flask import Flask, request,jsonify
from flask import render_template
import db

# _name_ 代表目前執行的模組
app=Flask(__name__) 


# 測試資料
tpe = {
    "id":0,
    "city name" : "Taipei",
    "country_name" : "Taiwan",
    "location" : {
        "log" : 121.569649,
        "lat" : 25.036786
    }
}

nyc = {
    "id":0,
    "city name" : "New York",
    "country_name" : "USA",
    "location" : {
        "log" : -74.00324,
        "lat" : 40.710234
    }
}

cities = [tpe,nyc]


# dict
users = [{"username": "高誠鴻", "url":"harrykao.gitio.com"},
        {"username": "林紫涵", "url":"10646028.gitio.com"},
        {"username": "zzz涵", "url":"10646028.gitio.com"}]


# ---------------------- 資料萃取測試 -----------------------
landmarks = list(db.getPLACE(['1144120088','GOGOG']))
print(landmarks[0])

# Tname = db.getTnames(['1144120088'])
# print(Tname)

addresses = db.getPlaceDetail([landmarks[0]])
print(addresses[0])

# ------------- 程式區 ------------------------

# 函式裝飾:以函式為基礎 提供附加功能
@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")



# 代表我們要處理的網站路徑
@app.route("/cities/all",methods=['GET'])
def cities_all():
    return jsonify(cities)


@app.route("/user/all",methods=['GET'])
def user_all():
    return render_template("user.html",users=users)

# 景點+Tname
@app.route("/place/all",methods=['GET'])
def place_all():
    Tname = db.getTnames(['1144120088'])
    landmarks = list(db.getPLACE(['1144120088','ASD']))
    return render_template("place.html", places = landmarks ,TravelName = Tname)


# 景點上去index.html
@app.route("/test1/all",methods=['GET'])
def test1_all():
    Tname = db.getTnames(['1144120088'])
    landmarks = list(db.getPLACE(['1144120088','ASD']))
    address = db.getPlaceDetail([landmarks])
    return render_template("test1.html", places = landmarks ,TravelName = Tname)






# 如果test.py為主程式 讓Web API 跑起來
if __name__=="__main__":
    app.run()

    