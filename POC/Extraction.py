from POC.Connection import *


# def extractDatasource(conn):
#     cursor = conn.cursor()
#     cursor.execute("USE MDEDB")
#     try:
#         cursor.execute(
#             "CREATE TABLE IF NOT EXISTS DATASOURCEMD(DatasourceId INT NOT NULL AUTO_INCREMENT, Datasource VARCHAR(255), PRIMARY KEY(DatasourceId))")
#     except Exception as err:
#         print("DATASOURCEMD already exists")
#     try:
#         cursor.execute("INSERT INTO DATASOURCEMD(Datasource) VALUES ('mysql')")
#     except Exception as err:
#         print("datasource already exists")
#     return


def schemaMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.tables().fetchall()
    result = set()
    for r in rs:
        schema = r.table_cat
        result.add(schema)
    closeConnection(conn)
    return result


def tableMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.tables().fetchall()
    result = []
    for r in rs:
        schema = r.table_cat
        table = r.table_name
        row = [table, schema]
        result.append(row)
    closeConnection(conn)
    return result


def attributeMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.columns().fetchall()
    result = []
    for r in rs:
        schema = r.table_cat
        table = r.table_name
        column = r.column_name
        type_name = r.type_name
        column_size = r.column_size
        row = [schema, table, column, type_name, column_size]
        result.append(row)
    closeConnection(conn)
    return result


def mappingMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.foreignKeys().fetchall()
    result = []
    for r in rs:
        pktable_cat = r.pktable_cat
        pktable_schem = r.pktable_schem
        pktable_name = r.pktable_name
        pkcolumn_name = r.pkcolumn_name
        fktable_cat = r.fktable_cat
        fktable_schem = r.fktable_schem
        fktable_name = r.fktable_name
        fkcolumn_name = r.fkcolumn_name
        pk_name = r.pk_name
        fk_name = r.fk_name
        row = [pktable_cat, pktable_schem, pktable_name, pkcolumn_name, fktable_cat, fktable_schem, fktable_name,
               fkcolumn_name, pk_name, fk_name]
        result.append(row)
    closeConnection(conn)
    return result
