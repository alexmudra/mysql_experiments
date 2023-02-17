import mysql.connector
import click

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='koba', host='127.0.0.1', port=3306 ,  database='local_koba')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from shop'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchone();
print("fetchone selection result:", result) #fetchone selection result: (1, 'Kolo', 'Kyiv, Sahaidachnogo st 2')

# The fetchmany() method is similar to the fetchone() but, it retrieves the next set of rows in the result set of a query, instead of a single row.
result = cursor.fetchmany(2);
print("fetchmany selection result:", result) #fetchmany selection result: [(2, 'ATB', 'Kyiv, Dovbusha st 10'), (3, 'Silpo', 'Teatralna street 45')]

#Fetching 1st row from the table
result = cursor.fetchall();
print(f"fetall selection:",result) #fetall selection: [(2, 'ATB', 'Kyiv, Dovbusha st 10'), (3, 'Silpo', 'Teatralna street 45'),
# (4, 'Kolo', 'Kyiv, Sahaidachnogo st 2'), (5, 'ATB', 'Kyiv, Dovbusha st 10'),
# (6, 'Silpo', 'Teatralna street 45'), (7, 'Kolo', 'Kyiv, Sahaidachnogo st 2'), (8, 'ATB', 'Kyiv, Dovbusha st 10'), (9, 'Silpo', 'Teatralna street 45')]



#Closing the connection
conn.close()