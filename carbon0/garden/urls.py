from django.urls import path
from .views import (
    LeafCreate,
    PlantCreate,
    PlantDetail,
    PersonalPlantList,
)


app_name = "garden"

urlpatterns = [
    path("plant/<int:plant_id>/leaf-check/", LeafCreate.as_view(),
         name="leaf_create"),
    path("plant/<slug:slug>/", PlantDetail.as_view(), name="plant_detail"),
    path("plant/create/", PlantCreate.as_view(), name="plant_create"),
    path("plant-list/", PersonalPlantList.as_view(), name="plant_list"),
]
