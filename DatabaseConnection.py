import mysql.connector

mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="qa123",
            database="user"
            )
mycursor=mydb.cursor()
mycursor.execute("create table my_table(id int primary key,Name varchar(50),Age int, Address varchar(50)")