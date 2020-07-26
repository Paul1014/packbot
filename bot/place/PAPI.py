import googlemaps
import json

gmaps = googlemaps.Client(key='AIzaSyABrj1Q38oMpuQ6z7IwkorLnnuYHxzFq_0')

def getNear(county,types):
    if types == "特色商圈":
        types = "商圈"
    elif types == "古蹟廟宇":
        types = "古蹟"
    elif types == "人文藝術":
        types = "博物館"
    #關鍵字搜尋
    geocode_result = gmaps.geocode(county+' '+types)
    loc = geocode_result[0]['geometry']['location']
    c = county+ ' '+types
    #創建序列存放
    ids = []

    #將半徑500公尺內的咖啡廳存放至ids序列
    for place in gmaps.places_nearby(keyword=c,location=loc, radius = 500)['results']:
        ids.append(place['place_id'])

    #用set存放資料消除重複元素
    stores_info = []
    ids = list(set(ids))

    #存放半徑500公尺內咖啡廳的名稱、位置、總評分數量、評分
    for id in ids:
        stores_info.append(gmaps.place(place_id=id,fields=['name', 'place_id', 'formatted_phone_number', 'formatted_address', 'geometry/location', 'opening_hours', 'user_ratings_total', 'rating'], language='zh-TW')['result'])
    
    #除去評論數太少以致沒有評分的店家
    delete = []
    for i in stores_info:
        if 'rating' not in i:
            delete.append(i)
    for j in delete:
        stores_info.remove(j)
    
    #依照評分數值由高至低進行排序，若評分相同則比較總評分數量

    stores_info = sorted(stores_info,key=lambda x: (x['rating'],x['user_ratings_total']),reverse=True)

    #抓出每個地址的相關資料(沒用到就不用看)
    lat = []
    lng = []
    name = []
    rating = []
    urt = []

    for i in stores_info:
        lat.append(dict(dict(dict(i)['geometry'])['location'])['lat'])
        lng.append(dict(dict(dict(i)['geometry'])['location'])['lng'])
        name.append(dict(i)['name'])
        rating.append(dict(i)['rating'])
        urt.append(dict(i)['user_ratings_total'])

    #輸出json檔
    #with open('APIP.json', 'w', encoding='utf-8') as f:
        #json.dump(stores_info, f)
    
    a=[]

    for i in range(0,5):
        if len(stores_info) <= i:
            break
        else:
            a.append(stores_info[i])
    aName = []
    for i in a:
        b = {'name':i['name'],'placeid':i['place_id']}
        aName.append(b)

    
    return aName


def getPlace(a):
    getP = gmaps.place(place_id=a, fields=['name', 'formatted_address', 'formatted_phone_number', 'geometry/location', 'opening_hours', 'user_ratings_total', 'rating'] ,language='zh-TW')
    b = getP['result']
    c = {}
    for i in b:
        if i != 'geometry' and i != 'opening_hours':
            d = b[i]
            e = {i:d}
            c.update(e)
        elif i == 'opening_hours':
            d = b[i]
            e = {'weekday_text':d['weekday_text']}
            c.update(e)
        elif i == 'geometry':
            e = b[i]
            d = e['location']
            c.update(d)
    return c

def getSearch(place):
    
    getS = gmaps.find_place(input=place, input_type='textquery', language='zh-TW')
    place_info = getS['candidates'][0]
    getP = gmaps.place(place_id=place_info['place_id'], fields=['name', 'formatted_address', 'formatted_phone_number', 'geometry/location', 'opening_hours', 'user_ratings_total', 'rating'] ,language='zh-TW')
    return getP