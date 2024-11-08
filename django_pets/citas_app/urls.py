from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("nueva", views.v_nueva, name="nueva"),
    path("lista", views.v_lista, name="lista"),
    path("reporte_xls", views.v_reporte_xls, name="reporte_xls"),
    path("reporte_pdf", views.v_generar_pdf, name="reporte_pdf")
]


# para ejecutar en el navegador mas rapido:

# /citas/reporte_xls
 
# /citas/reporte_pdf
 

#  para instalar libreria que genera pdf:
# pip install reportlab   
 