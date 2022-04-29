pip install mysql-connector-python
#to use database import abouve module in cmd

import mysql.connector
cnx=mysql.connector.connect(user='root',password='',host='localhost',database='asdasd')

cursor = cnx.corsor()

def add():
	email=input("Enter email:")
	password=input("Enter password:")
	city=input("Enter city:")
	mobile=int(input("Enter mobile:"))

	query= "INSERT INTO users VALUES (NULL,%s,%s,%s,%s)"
	corsor.execute(query,email,password,city,mobile,2)
	cnx.commit()
	print("data added sussesfully!!!!")
	# at the time of close

def view():
	query="SELECT users.*,collage.collage_name FROM users INNER JOIN collages ON users.collage_id=collages.id"
	cursor.execute(query)
	result = cursor.fetchall()
	print("\t\t\tt----------------------user deatials----------------------")
	string1="{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("Id","email","password","city","mobile","collage_id","collage name")
	print(string1)
	print("--------------------------------------------------------------------------")

	for data in sesult:
		for row in data:
			string1="{:^20}".format(row)
			print(string1, end=" ")
		print("\n")
		cnx.commit()
		#at the time of close

	choice=1
	while choice!=1:
		print("------ welcome to student database deatials----------------------")
		choice=int(input("select Operation 1. add 2.view 3. Exit:"))
		if choice==1:
			add()
		if choice==2:
			view()
		if choice==3:
			break
	else:
		print("Thank you kaka!")

	cursor.close()
	cnx.close()