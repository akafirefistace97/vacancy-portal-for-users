# import the library

import mysql.connector

#connection to databases
conn=mysql.connector.connect(user='root',password='',host='localhost',database='python')

#cursor is like a driver which is use a get and fetch the data
cursor=conn.cursor()
choice= int(input("Choose the action 1.Add, 2.view, 3.edit, 4.delete:"))

if choice==1:
	email=input("Enter email:")
	password=input("Enter password:")
	city=input("Enter city:")
	mobile=input("Enter mobile:")
	collage_id=input("Enter collage_id:")
	birth_date=input("Enter birth_date:")
	que="INSERT INTO users VALUES(NULL,%s,%s,%s,%s,%s,%s) "
	cursor.execute(que,(email,password,city,mobile,collage_id,birth_date))




if choice==2:
	#query
	que="SELECT * FROM users INNER JOIN colleges ON users.collage_id=collages.id "

	#query exicution
	cursor.execute(que)

	#fetch the data into the databases
	result=cursor.fetchall()


	for i in result:
		for j in i:
			print("\t",j,  end=" ")
		print()
#if choice==3:
#if choice==4:








conn.commit()
#connection close
cursor.close()
conn.close()