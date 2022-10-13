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
        fields = ("id", "name", "description")


class DatasetSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    datasource = DatasourceSerializer(read_only=True)
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'


class DatasetListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()


class DatasetRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()


class FieldUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
