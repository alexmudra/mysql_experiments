import mysql.connector
import click
from mysql.connector import ProgrammingError


@click.command()
@click.option('--host', default="localhost", help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', help='Database username')
@click.option('--password', help='Database password')
@click.option('--database', help='Database to user')
@click.option('--shop_name', help='Set shop name to search assortiment in')
@click.option('--shop_address', help='Shop address')
def show_items_in_shop(host, port, username, password, database, shop_name, shop_address):
    db_connector = mysql.connector.connect(user=username, password=password, host=host, port=port, database=database)
    cursor = db_connector.cursor()
    try:
        cursor.execute("SELECT i.ITEM_NAME as ITEM_NAME, i.PRICE as "
                   "PRICE FROM shop s "
                   "LEFT JOIN item_shop ish "
                   " ON s.ID = ish.SHOP_ID"
                   " LEFT JOIN item i "
                   "ON i.ID = ish.ITEM_ID "
                   "WHERE s.NAME = %(shop_name)s "
                   "AND s.ADDRESS = %(shop_address)s",
                   {"shop_name": shop_name, "shop_address": shop_address})
    except ProgrammingError:
        print(f"Bad query: {cursor.statement}")

    result = cursor.fetchall()

    if not result:
        print("No shop is found or no items in it")
    else:
        for it in result:
            print(f"Item name: {it[0]}. Price: {it[1]}")

    db_connector.close()

if __name__ == "__main__":
    show_items_in_shop()

#команда для запуску в терміналі (my_venvs) C:\Users\alex\PycharmProjects\mysqlcursorexample>python shop_items_in_shop.py --username root --password koba --database some_db --shop_name ATB --shop_address "Kyiv, Syretska street 3"
