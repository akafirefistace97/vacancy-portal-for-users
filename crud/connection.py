# import the library

import mysql.connector

#connection to databases
conn=mysql.connector.connect(user='root',password='',host='localhost',database='python')

#cursor is like a driver which is use a get and fetch the data
cursor=conn.cursor()

#query
que="SELECT * FROM users "

#query exicution
cursor.execute(que)

#fetch the data into the databases
result=cursor.fetchall()


for i in result:
	for j in i:
		print("\t",j,  end=" ")
	print()







conn.commit()
#connection close
cursor.close()
conn.close()