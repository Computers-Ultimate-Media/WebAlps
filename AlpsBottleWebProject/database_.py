import mysql.connector  # pip install mysql-connector-python
from mysql.connector import errorcode

HOST = "localhost"
USER = "root"
PASSWORD = "root"

db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    use_pure=True)


def make_database_and_table():
    cursor = db.cursor()
    db_name = 'bottle_db'

    def create_db(cursor):
        try:
            cursor.execute("create database {}".format(db_name))
            print("Database created.")
        except mysql.connector.Error as err:
            print("Database creation failed:", err)
            exit(1)

    try:
        db.database = db_name
        print('Database {} already exist.'.format(db_name))
    except mysql.connector.Error as err:
        # database doesn't exist, create one
        if errorcode.ER_BAD_DB_ERROR == err.errno:
            create_db(cursor)
            db.database = db_name
    try:
        cursor.execute(
            "CREATE TABLE if not exists stuff (id INT AUTO_INCREMENT PRIMARY KEY, login VARCHAR(45), email VARCHAR(45))")
    except mysql.connector.Error as err:
        if errorcode.ER_TABLE_EXISTS_ERROR == err.errno:
            print('Table stuff already exists.')


def data_from_base(sql_: str, f_all: bool):
    my_cursor = db.cursor()
    my_cursor.execute(sql_)
    if f_all:
        my_result = my_cursor.fetchall()
    else:
        my_result = my_cursor.fetchone()
    return my_result


def insert_data_in_base(sql_: str, val_: any):
    my_cursor = db.cursor()
    try:
        my_cursor.execute(sql_, val_)
        db.commit()
    except mysql.connector.Error as error:
        pass
