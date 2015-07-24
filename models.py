import sqlite3 as sql

def insert_link(key,url,hits):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO link (key,url,hits) VALUES (?,?,?)", (key,url,hits))
		con.commit()

def query_hits_and_url_for_link(key):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		key = str(key)
		cur.execute("SELECT * FROM link WHERE key=?", (key,))
		link_data = cur.fetchall()
		print link_data
		return link_data

def update_hits(key):
	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("UPDATE link SET hits = (hits + 1) WHERE key=key")
		con.commit()