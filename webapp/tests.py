
from POC.Connection import *

conn = openConnection()
cursor = conn.cursor()
rs=cursor.foreignKeys().fetchall()
for r in rs:
    print(r)

