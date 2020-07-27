import sqlite3

conn = sqlite3.connect("URL.sqlite")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Urls (id integer unique Primary Key, original_urls text, short_urls text)")


def check(url):
	cur.execute("SELECT original_urls FROM Urls WHERE original_urls= ?",(url, ))
	out = cur.fetchone()
	if out is None:
		return 1
	else:
		return 0

def fetchShortOf(url):
	for out in cur.execute("SELECT short_urls FROM Urls WHERE original_urls = ?",(url, )) :
		return str(out[0])

def insertOriginal(url):
	cur.execute("INSERT INTO Urls (original_urls) VALUES(?)",(url,))
	id = cur.execute("SELECT id FROM Urls WHERE original_urls = ? " ,(url,))
	for row in id:
		return int(row[0])
	conn.commit()
	

def insert(original, short):
	cur.execute("DELETE FROM Urls WHERE original_urls= ?",(original, ))
	cur.execute("INSERT INTO Urls (original_urls, short_urls) VALUES (? , ?)",(original, short))
	conn.commit()