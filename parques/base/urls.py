from django.urls import path

from parques.base.views import base, parque_layout_1, parque_layout_2

app_name = "base"
urlpatterns = [
    path("", base, name="base"),
    path("parque_layout_1/", parque_layout_1, name="parque_layout_1"),
    path("parque_layout_2/", parque_layout_2, name="parque_layout_2"),
]
