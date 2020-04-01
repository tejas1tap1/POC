from rest_framework import serializers
from .models import *

class datasourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Datasource
        fields = '__all__'

class schemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schema
        fields = '__all__'

class tableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'

class attributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = '__all__'

class mappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mapping
        fields = '__all__'