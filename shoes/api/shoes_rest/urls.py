from django.urls import path

from .views import (
    api_list_shoes, api_detail_shoe,
)

urlpatterns = [
    path("shoes/", api_list_shoes, name="api_list_shoes"),
    path(
        "shoes/<int:pk>/", api_detail_shoe, name="api_detail_shoe",
    ),
]
