from django.db import models
from django.utils.translation import gettext_lazy as _


class Datasource(models.Model):
    name = models.CharField(max_length=300, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=300, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name


class Dataset(models.Model):
    name = models.CharField(max_length=300, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, verbose_name=_("Owner"))
    datasource = models.ForeignKey(
        Datasource, on_delete=models.PROTECT, verbose_name=_("Datasource")
    )

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=300, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.PROTECT,
        verbose_name=_("Dataset"),
        related_name="fields",
    )

    def __str__(self):
        return f"{self.name} - {self.dataset}"
