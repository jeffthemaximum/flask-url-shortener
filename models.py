import os
import pudb
import psycopg2
import urlparse

#for heroku:
#urllib.parse.uses_netloc.append("postgres")
#url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
url = urlparse.urlparse("postgres://zcatrfpbvdgxdl:3t-ulfLl-5PA42XiQt3Vj8zoAk@ec2-54-235-134-167.compute-1.amazonaws.com:5432/d526v5gjqufm10")

con = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

def insert_link(key,url,hit):
	cur = con.cursor()
	query = "INSERT INTO link (key,url,hit) VALUES (%s,%s,%s);" 
	data = (key,url,hit)
	cur.execute(query, data)
	con.commit()

def query_hits_and_url_for_link(key):
	cur = con.cursor()
	key = str(key)
	query = "SELECT * FROM link WHERE key=%s;"
	data = (key,)
	cur.execute(query, data)
	link_data = cur.fetchall()
	print link_data
	return link_data

def update_hits(key):
	cur = con.cursor()
	cur.execute("UPDATE link SET hit = (hit + 1) WHERE key=key")
	con.commit()