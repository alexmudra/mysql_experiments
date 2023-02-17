import mysql.connector
import click


@click.command()
@click.option('--host', default="localhost", help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', help='Database username')
@click.option('--password', help='Database password')
@click.option('--database', help='Database to user')
def create_table(host, port, username, password, database):
    db_connector = mysql.connector.connect(user=username, password=password, host=host, port=port, database=database)
    cursor = db_connector.cursor()

    # Create bar table
#     cursor.execute("""
#     CREATE TABLE shop (
# ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# NAME VARCHAR(150) NOT NULL,
# ADDRESS VARCHAR(250) NOT NULL
# )
#     """)

#     # Create item table
#     cursor.execute("""
#     CREATE TABLE item (
# ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# ITEM_NAME VARCHAR(250) NOT NULL,
# PRICE FLOAT NOT NULL
# );
#     """)

    #Create intermediate table to store one item in multiple tables
    cursor.execute("""
     CREATE TABLE item_shop (
     ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
     SHOP_ID INT NOT NULL,
     ITEM_ID INT NOT NULL,
     FOREIGN KEY (SHOP_ID) REFERENCES shop(ID),
     FOREIGN KEY (ITEM_ID) REFERENCES item(ID)
     )
     """)

    db_connector.close()

if __name__ == "__main__":
    create_table()

#запуск команди в терміналі python create_table_in_db.py --username root --password koba --database Local_koba
