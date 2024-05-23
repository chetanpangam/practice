# mysqlConnector.py



import mysql.connector

print("==== DB Connect =====")

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password= "password"
	)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mydatabase")

print("======= DB Crete ======")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

mycursor.execute("CREATE DATABASE mydatabase")
print("Created the database")

mydb.close()

print("========= Create Table =========")

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "password",
	database = "mydatabase"
	)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(id int AUTO_INCREMENT PRIMARY KEY, name varchar(255), city varchar(255))")
print("Table created")


print("========= Insert into table =========")

sql = "INSERT INTO customers(name, city) values (%s, %s)"
val = [
		("Chetan", "SJC"),
		("Shruti", "BOM"),
		("Pragati", "BOS")
		]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "Record inserted")


print("====== Select from Database ========")

mycursor.execute("SELECT name, city from customers")

myresult = mycursor.fetchall()

for data in myresult:
	print(data)

print("======== Delete Record ========")

sql = "DELETE FROM customers where name = %s"
val = ("Pragati",)
mycursor.execute(sql, val)

mydb.commit()
print("Record deleted")

print("====== Select from Database ========")

mycursor.execute("SELECT name, city from customers")

myresult = mycursor.fetchall()

for data in myresult:
	print(data)

print("===== Drop Table ========")

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
print("Dropped the table")

print("======== Drop DB ===========")

mycursor.execute("DROP DATABASE mydatabase")
print("Dropped the database")