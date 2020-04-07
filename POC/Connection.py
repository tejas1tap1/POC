import pyodbc


class ConnectionParams:
    def __init__(self, driver, url, port, database, user, password):
        self.driver = driver
        self.url = url
        self.port = port
        self.database = database
        self.user = user
        self.password = password


def openConnection(ConnectionParams):
    # url = "127.0.0.1"
    # port = "3306"
    # database = "shopping"
    # user = "root"
    # password = "tejas1234"
    url = ConnectionParams.url
    port = ConnectionParams.port
    database = ConnectionParams.database
    user = ConnectionParams.user
    password = ConnectionParams.password
    conn = None
    try:
        conn = pyodbc.connect(
            'DRIVER=MySQL ODBC 8.0 ANSI Driver;SERVER=' + url + ';PORT=' + port + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password + ';charset =utf8mb4;')
    except Exception as err:
        print("connection failed" + " " + err.__str__())
    return conn


def closeConnection(conn):
    conn.close()
