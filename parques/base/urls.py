from django.urls import path

from parques.base.views import base, parque_individual

app_name = "base"
urlpatterns = [
    path("", base, name="base"),
    path("parque-individual/", parque_individual, name="parque_individual"),
]
