import sqlite3

def setTname(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute('insert into User(UserID, Tname) values (?,?)', data)
	connection.commit()

def setCOUNTY(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute('UPDATE User SET COUNTY = ? WHERE UserID LIKE? AND Tname LIKE?', data)
	connection.commit()

def setTYPE_one(data):
	print(type(data))
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("UPDATE User SET TYPE_one = ? WHERE UserID LIKE? AND Tname LIKE?",data)
	connection.commit()

def setTYPE_two(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("UPDATE User SET TYPE_two = ? WHERE UserID LIKE? AND Tname LIKE?",data)
	connection.commit()

def setTYPE_three(data):
	connection = sqlite3.connect('db/test.db')
	
	c = connection.cursor()
	c.execute("UPDATE User SET TYPE_three = ? WHERE UserID LIKE?  AND Tname LIKE?",data)
	connection.commit()

def setPlace(times,data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	print(data)
	print(type(data))
	if times == 1:
		c.execute("UPDATE User SET Place_one = ? WHERE UserID LIKE?  AND Tname LIKE?",data)
	elif times == 2:
		c.execute("UPDATE User SET Place_two = ? WHERE UserID LIKE?  AND Tname LIKE?",data)
	elif times == 3:
		c.execute("UPDATE User SET Place_three = ? WHERE UserID LIKE?  AND Tname LIKE?",data)
	elif times == 4:
		c.execute("UPDATE User SET Place_four = ? WHERE UserID LIKE?  AND Tname LIKE?",data)
	elif times == 5:
		c.execute("UPDATE User SET Place_five = ? WHERE UserID LIKE?  AND Tname LIKE?",data)

	connection.commit()

def setPlacedetail(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute('insert into Place(PlaceName, Address, Rating, Phone, Time) values (?,?,?,?,?)',data)
	connection.commit()

def getTYPE(data): #input list type
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("SELECT TYPE_one, TYPE_two, TYPE_three FROM User WHERE UserID LIKE? AND Tname LIKE?",data)
	types = c.fetchone()
	return types #return is tunple type

def getCOUNTY(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("SELECT COUNTY FROM User WHERE UserID LIKE? AND Tname LIKE?",data)
	county = c.fetchone()
	return county

def getPLACE(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("SELECT Place_one, Place_two, Place_three, Place_four, Place_five FROM User WHERE UserID LIKE? AND Tname LIKE?",data)
	place = c.fetchone()
	return place

def getPlaceDetail(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("SELECT Address, Rating, Phone, Time FROM Place WHERE PlaceName LIKE? ",data)
	PlaceDetail = c.fetchone()

	return PlaceDetail

def getTnames(data):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("SELECT Tname FROM User WHERE UserID LIKE? ",data)
	Tnames = c.fetchall()

	return Tnames

def Deleterecord(ID):
	connection = sqlite3.connect('db/test.db')
	c = connection.cursor()
	c.execute("DELETE FROM User WHERE UserID LIKE? ",ID)
	connection.commit()

print(getTnames(['1144120088']))
#print(getPlaceDetail( ['臺北市兒童新樂園'] ))
