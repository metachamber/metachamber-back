from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.DatasetListAPIView.as_view(), name="dataset_list"),
]
