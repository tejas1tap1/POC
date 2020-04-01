from django.db import models

# Create your models here.

class Datasource(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=256)
    version = models.CharField(max_length=256)

    def __str__(self):
        return self.type

class Schema(models.Model):
    id=models.AutoField(primary_key=True)
    databaseName=models.CharField(max_length=256)
    datasourceId = models.ForeignKey(Datasource, on_delete=models.CASCADE)

    def __str__(self):
        return self.databaseName


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    tableName = models.CharField(max_length=256)
    schemaId = models.ForeignKey(Schema, on_delete=models.CASCADE)
    datasourceId = models.ForeignKey(Datasource, on_delete=models.CASCADE)

    def __str__(self):
        return self.tableName

class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    columnName = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    key = models.CharField(max_length=256, blank=True)
    tableId = models.ForeignKey(Table, on_delete=models.CASCADE)
    schemaId = models.ForeignKey(Schema, on_delete=models.CASCADE)
    datasourceId = models.ForeignKey(Datasource, on_delete=models.CASCADE)

    def __str__(self):
        return self.columnName

class Mapping(models.Model):
    attributeIdForeignKey = models.IntegerField()
    tableIdForeign = models.IntegerField()
