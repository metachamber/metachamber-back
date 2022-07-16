from django.shortcuts import render
from rest_framework import serializers, generics

from catalog.models import Datasource, Owner, Dataset, Field


class DatasourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datasource
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ("name", "description")


class DatasetSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    datasource = DatasourceSerializer()
    fields = FieldSerializer(many=True)

    class Meta:
        model = Dataset
        fields = '__all__'


class DatasetListAPIView(generics.ListAPIView):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()
