from django.urls import path

from catalog import views

urlpatterns = [
    path("dataset/", views.DatasetListCreateAPIView.as_view(), name="dataset"),
    path("dataset/<int:pk>/", views.DatasetRetrieveUpdateAPIView.as_view(), name="a_dataset"),
    path("field/<int:pk>/", views.FieldUpdateAPIView.as_view(), name="a_field"),
]
