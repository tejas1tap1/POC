import pyodbc


def openConnection():
    conn = None
    try:
        conn = pyodbc.connect('DRIVER=MySQL ODBC 8.0 ANSI Driver;SERVER=127.0.0.1;PORT=3306;DATABASE=shopping;UID=root;PWD=tejas1234;charset =utf8mb4;')
    except Exception as err:
        print("connection failed" + " " + err.__str__())
    return conn


def closeConnection(conn):
    conn.close()
