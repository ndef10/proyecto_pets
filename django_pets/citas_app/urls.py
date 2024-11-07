from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("nueva", views.v_nueva, name="nueva"),
    path("lista", views.v_lista, name="lista"),
    path("reporte", views.v_reporte, name="reporte")
]