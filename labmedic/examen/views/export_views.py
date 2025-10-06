from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from django.http import FileResponse
import io
from ..models import Examen
from openpyxl import Workbook




def exportar_examenes_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 14)
    p.drawString(2*cm, height - 2*cm, "LABMEDIC - Reporte de Exámenes Clínicos")

    y = height - 3*cm
    p.setFont("Helvetica", 10)

    for examen in Examen.objects.all():
        total = examen.calcular_total()
        p.drawString(2*cm, y, f"{examen.nombre} ({examen.categoria.nombre}) - S/ {total}")
        y -= 0.7*cm
        if y < 2*cm:
            p.showPage()
            y = height - 2*cm

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="examenes_labmedic.pdf")



def exportar_examenes_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Exámenes Clínicos"

    ws.append(["Nombre", "Categoría", "Precio Total"])

    for examen in Examen.objects.all():
        ws.append([
            examen.nombre,
            examen.categoria.nombre,
            examen.calcular_total()
        ])

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return FileResponse(output, as_attachment=True, filename="examenes.xlsx")
