from sqlite3 import Error, connect

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
            self.connection = connect('/home/pepper/PycharmProjects/PokerBotTeleg/DB/dbrecords')
        return self.connection

    @staticmethod
    def add_posts(args):
        try:
            connection = connect('/home/pepper/PycharmProjects/PokerBotTeleg/DB/dbrecords')
            cursor = connection.cursor()

            sqlite_select_query = f"""SELECT * FROM records WHERE ID = {args[0]}"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            if records:
                return
            else:
                cursor.execute(f"INSERT INTO records VALUES {args}")
            connection.commit()

        except Exception as er:
            print("Failed in ADD method\n", er)
        finally:
            if (connection):
                connection.close()

    @staticmethod
    def setRows(tgID, stck: int):
        try:
            connection = connect('/home/pepper/PycharmProjects/PokerBotTeleg/DB/dbrecords')

            cursor = connection.cursor()
            sqlite_select_query = f"""SELECT Stack FROM records WHERE ID = {tgID}"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            if records[0][0] < stck:
                connection.execute(f'UPDATE records SET Stack = {stck} WHERE ID = {tgID}')
                connection.commit()
        except Exception as er:
            print("Failed in SET method\n", er)
        finally:
            if (connection):
                connection.close()

    @staticmethod
    def getRows():
        try:
            connection = connect('/home/pepper/PycharmProjects/PokerBotTeleg/DB/dbrecords')
            cursor = connection.cursor()

            sqlite_select_query = """SELECT NAME, STACK FROM records ORDER BY STACK DESC LIMIT 5"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            #all records, a[0] = id, a[1] = name, a[2] = stack
            cursor.close()
        except Exception as er:
            print("Failed in GET method\n", er)
        finally:
            if (connection):
                connection.close()
        return records

# create table *records*
# conn = connect('dbrecords')
# conn.execute('''CREATE TABLE records
#          (ID            INT      NOT NULL,
#          NAME           TEXT    NOT NULL,
#          STACK          INT );''')

# add test data
# Database.add_posts((4, 'name4test', 1234))
# Database.add_posts((2, 'name2test', 12))
# Database.add_posts((3, 'name3test', 123))

# example to outPutInfo
# print(Database.getRows())

# show all DB
# for i in connect('/home/pepper/PycharmProjects/PokerBotTeleg/DB/dbrecords').cursor().execute("""SELECT NAME, STACK FROM records ORDER BY STACK DESC""").fetchall():print(i)