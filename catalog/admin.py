from django.contrib import admin

from catalog.models import Datasource, Owner, Dataset, Field


@admin.register(Datasource)
class DatasourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass
