from POC.Connection import *
from webapp.models import *

def extractDatasource():
    datasource=None
    try:
        datasource = Datasource.objects.get(type='mysql', version='5.7.29')
    except:
        pass
    if datasource==None:
       datasource = Datasource(type='mysql', version='5.7.29')
    datasource.save()
    return


def schemaMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.tables().fetchall()
    result = set()
    for r in rs:
        schema = r.table_cat
        result.add(schema)
    for r in result:
        schema=None
        try:
           schema = Schema.objects.get(databaseName=r, datasourceId=Datasource.objects.get(type='mysql'))
        except:
            pass
        if schema==None:
            schema = Schema(databaseName=r, datasourceId=Datasource.objects.get(type='mysql'))
        schema.save()
    closeConnection(conn)
    return


def tableMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.tables().fetchall()
    for r in rs:
        schema = r.table_cat
        tableName = r.table_name
        table = None
        try:
            table = Table.objects.get(tableName=tableName, schemaId=Schema.objects.get(databaseName=schema),datasourceId=Datasource.objects.get(type='mysql'))
        except:
            pass
        if table==None:
           table = Table(tableName=tableName,schemaId=Schema.objects.get(databaseName=schema),datasourceId=Datasource.objects.get(type='mysql'))
        table.save()
    closeConnection(conn)
    return

def attributeMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.columns().fetchall()
    for r in rs:
        tableName = r.table_name
        column = r.column_name
        type = r.type_name
        table = Table.objects.get(tableName=tableName)
        attribute= None
        try:
            attribute = Attribute.objects.get(columnName=column,tableId=table, schemaId=table.schemaId,datasourceId=table.datasourceId)
        except:
            pass
        if attribute==None:
             attribute = Attribute(columnName=column, type=type, tableId=table, schemaId=table.schemaId,
                              datasourceId=table.datasourceId)
        attribute.save()
    rs2 = cursor.tables().fetchall()
    for r in rs2:
        tableName = r.table_name
        table = Table.objects.get(tableName=tableName)
        keys=cursor.primaryKeys(table.tableName).fetchall()
        for key in keys:
            columnName = key.column_name
            keyName = key.pk_name
            attribute = Attribute.objects.get(columnName=columnName, tableId=table)
            attribute.key = keyName
            attribute.save()
    closeConnection(conn)
    return


def mappingMetadata():
    conn = openConnection()
    cursor = conn.cursor()
    rs = cursor.foreignKeys().fetchall()
    for r in rs:
        pktable_cat = r.pktable_cat
        pktable_name = r.pktable_name
        pkcolumn_name = r.pkcolumn_name
        fktable_cat = r.fktable_cat
        fktable_name = r.fktable_name
        fkcolumn_name = r.fkcolumn_name
        pk_name = r.pk_name
        fk_name = r.fk_name
        fkSchema=Schema.objects.get(databaseName=fktable_cat)
        fkTable=Table.objects.get(tableName=fktable_name, schemaId=fkSchema)
        fkAttribute = Attribute.objects.get(columnName=fkcolumn_name, tableId=fkTable.id)
        pkSchema=Schema.objects.get(databaseName=pktable_cat)
        pkTable=Table.objects.get(tableName=pktable_name, schemaId=pkSchema)
        mapping = None
        try:
            mapping = Mapping.objects.get(attributeIdForeignKey=fkAttribute)
        except:
            pass
        if mapping==None:
           mapping = Mapping(attributeIdForeignKey=fkAttribute, tableIdForeign=pkTable)
        mapping.save()
    closeConnection(conn)
    return
