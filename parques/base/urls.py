from django.urls import path
from parques.base.views import base, parque_1, parque_2, parque_3

app_name = "base"

urlpatterns = [
    path("", base, name="base"),
    path("parque_1/", parque_1, name="parque_1"),
    path("parque_2/", parque_2, name="parque_2"),
    path("parque_3/", parque_3, name="parque_3"),
]
