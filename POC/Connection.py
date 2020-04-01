import pyodbc


def openConnection():
    conn = None
    try:
        conn = pyodbc.connect('DRIVER=MySQL ODBC 8.0 Driver;SERVER=localhost;PORT=3306;DATABASE=MDEDB;UID=root;PWD'
                              '=Swami@2309;charset =utf8mb4;')
    except Exception as err:
        print("connection failed" + " " + err.__str__())
    return conn


def closeConnection(conn):
    conn.close()
