import sqlite3

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("dbrecords")
        return self.connection

    def get_posts(db):
        with db:
            db.cursor().execute("SELECT * FROM records")
            print(db.cursor().fetchall())

    def set_posts(db, args):
        with db:
            db.cursor().execute(f"INSERT INTO records VALUES {args}")
            db.commit()


db1 = Database().connect()
# db1.cursor().execute("""CREATE TABLE records
#               (id text, fname text, stack int)
#           """)

Database.set_posts(db1,('1231_id','f mane123',123))
Database.set_posts(db1,('1231_id','f mane123',13123))
Database.set_posts(db1,('1231_id','f mane123',23))

Database.get_posts(db1)



def getAllRows():
    try:
        connection = sqlite3.connect('dbrecords')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from records"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The Sqlite connection is closed")

getAllRows()
