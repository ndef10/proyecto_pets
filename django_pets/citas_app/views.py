from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
import datetime

# ========================================================================
from reportlab.lib.pagesizes import A4  # <---- Libreria
from reportlab.pdfgen import canvas  
# =======================================================================
# Create your views here.

def index(request):
    return HttpResponse("Citas index")

def v_nueva(request):
    return HttpResponse("Citas nueva")

def v_lista(request):
    return HttpResponse("Citas lista")

# ===============================================================esto genera un documento de excel====================================
def v_reporte_xls(request):
    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Reporte de Ejemplo"

    # Agregar encabezados
    encabezados = ["ID", "Nombre", "Fecha"]
    worksheet.append(encabezados)

    # Agregar algunos datos de ejemplo
    datos = [
        [1, "Alice", datetime.date(2023, 11, 5)],
        [2, "Bob", datetime.date(2023, 11, 6)],
        [3, "Charlie", datetime.date(2023, 11, 7)],
    ]

    for fila in datos:
        worksheet.append(fila)

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=reporte.xlsx"

    # Guardar el libro en la respuesta
    workbook.save(response)

    return response

# =====================================================================desde aca genera pdf===========================================

def v_generar_pdf(request): #<----- View
    # Crear la respuesta HTTP con el tipo de contenido para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el objeto canvas de ReportLab para generar el PDF
    p = canvas.Canvas(response, pagesize=A4)
    ancho, alto = A4  # Tamaño de la página

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, alto - 100, "Hola, este es un PDF generado desde Django.")
    p.drawString(100, alto - 120, "Puedes personalizar este contenido como desees.")

    # Finalizar y cerrar el PDF
    p.showPage()
    p.save()

    return response
