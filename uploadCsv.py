#!/usr/bin/env python
# coding: utf-8



import mysql.connector
import csv





with open('pokemon_data.csv') as csv_file:
    csvfile=csv.reader(csv_file,delimiter=',')
    header=[]
    row1=[]
    #holding all the header as a collections
    for row in csvfile:
        header=row
        break
    #holding all the first record as a collections for inferschema
    i=0
    for row in csvfile:
        if i==1:
            row1=row
            break
        i=i+1
#print(header)
#print(row1)





datatyperow=[]
datatype_spec=[]
for col in row1:
    if col.isdigit():
        val=" INT(11),"
        spec="%s,"
    elif type(col)==str:
        val=" VARCHAR(100),"
        spec="%s,"
    datatyperow.append(val)
    datatype_spec.append(spec)
res = [i + j for i , j in zip(header, datatyperow)]
#create statement string like-->col_name data_type
create_state=""
create_state=create_state.join(res)
create_state=create_state[3:-1]#to eliminate primary key hashed elements
#insert statement String like-->%d
insert_state=""
insert_state=insert_state.join(datatype_spec)
insert_state=insert_state[:-1]
#header name used for create insert statement
header_str=","
header_str=header_str.join(header)
header_str=header_str[3:]#to eliminate primary key hashed elements
#print(header_str)
#print(insert_state)





with open('pokemon_data.csv') as csv_file:
    csvfile=csv.reader(csv_file,delimiter=',')
    all_values=[]
    header=[]
    row1=[]
    #holding all the records as a collections
    i=0
    for row in csvfile:
        if i==0:
            i=1
            continue
        tuple_row=tuple(row)
        all_values.append(tuple_row)
#print(all_values)




db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)




mycursor = db.cursor()





mycursor.execute("CREATE DATABASE csvFile_db")





mycursor.execute("use csvFile_db");





mycursor.execute("CREATE TABLE filename ("+create_state+")")





sql = "INSERT INTO filename ("+header_str+") VALUES ("+insert_state+")"






mycursor.executemany(sql,all_values)

db.commit()

print(mycursor.rowcount, "was inserted.")







