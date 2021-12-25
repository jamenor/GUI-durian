# database.py

import sqlite3

conn = sqlite3.connect('product-datavase.sqlite3')
c = conn.cursor()

#create table
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quan REAL,
				total REAL )""")

print('Success')

def insert_transaction(data):
	# data = {'tid':'1234234','stamp':'2021-12-12 10:20:59'....}
	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quan = data['quan']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quan,total))
		conn.commit()
	print('inserted!')


def view_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)

transaction = {'tid':'123456782',
			   'stamp': '2021-12 11:46:20',
			   'product':'ทุเรียน',
			   'price':100,
			   'quan':50,
			   'total':5000}



# insert_transaction(transaction)

view_transaction()
