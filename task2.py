import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='Sumiya@1919', database='example')

try:
    print(con.connection_id, "Connection successfull")

except:
    print("Connection Failure")

#Instatiation of Cursor object
curobj = con.cursor()
#Table creation
#q1 = 'create table Product(price integer,name varchar(20) UNIQUE, period integer)'
#curobj.execute(q1)

#Data creation
q3 = 'insert into Product values(%s, %s, %s)'
rec1 = (2000,'cycle',178)
rec2 = (8000,'realme7',256)
rec3 = (6000,'realme6',198)

#curobj.execute(q3, rec1)
#curobj.execute(q3, rec2)
#curobj.execute(q3, rec3)
#curobj.executemany(q3, whitelist)
#con.commit()

#q4 = 'select * from Product'
#curobj.execute(q4)
#res = curobj.fetchall()
#for val in res:
 #   print(val)
print("using like")

sql = "SELECT * FROM Product WHERE name LIKE '%realme%'"

curobj.execute(sql)

myresult = curobj.fetchall()

for x in myresult:
  print(x)

print("using or")
sql1 = "SELECT * FROM Product WHERE price BETWEEN 1500 AND 2000 OR period BETWEEN 180 AND 200"


curobj.execute(sql1)

myresult1 = curobj.fetchall()

for x in myresult1:
  print(x)

print("using and")

sql2 = "SELECT * FROM Product WHERE price >=1500 AND price <=2000 and period >=160  AND period <=200"
curobj.execute(sql2)

myresult2 = curobj.fetchall()

for x in myresult2:
  print(x)

print("deleting")

sql3 = "DELETE FROM Product where name='cycle'"
curobj.execute(sql3)

myresult3 = curobj.fetchall()

#for x in myresult3:
 # print(x)

print("after delete")
q4 = 'select * from Product'
curobj.execute(q4)
res = curobj.fetchall()
for val in res:
    print(val)

sql4 = "UPDATE Product SET price ='500000' where name='realme7'"
curobj.execute(sql4)
resul = curobj.fetchall()
for val in resul:
    print(val)
q4 = 'select * from Product'
curobj.execute(q4)
res = curobj.fetchall()
for val in res:
    print(val)


