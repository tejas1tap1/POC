from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from rest_framework import status
from . serializers import *
from POC.Extraction import *

# Create your views here.
class DatasourceList(APIView):

    def get(self, request):
        extractDatasource()
        datasourceList = Datasource.objects.all()
        serializer= datasourceSerializer(datasourceList, many=True)
        return Response(serializer.data)

class SchemaList(APIView):

    def get(self, request):

        schemaMetadata()
        schemaList = Schema.objects.all()
        serializer = schemaSerializer(schemaList, many=True)
        return Response(serializer.data)

class TableList(APIView):

    def get(self, request):

        tableMetadata()
        tableList = Table.objects.all()
        serializer = tableSerializer(tableList, many=True)
        return Response(serializer.data)

class AttributeList(APIView):

    def get(self, request):

        attributeMetadata()
        attributeList = Attribute.objects.all()
        serializer = attributeSerializer(attributeList, many=True)
        return Response(serializer.data)

class MappingList(APIView):

    def get(self, request):
        Mapping.objects.all().delete()
        mappingMetadata()
        mappingList = Mapping.objects.all()
        serializer = mappingSerializer(mappingList, many=True)
        return Response(serializer.data)