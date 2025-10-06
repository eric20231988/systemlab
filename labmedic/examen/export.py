import io
from openpyxl import Workbook
from django.http import FileResponse
from .models import TipoExamen

def exportar_examenes_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Tipos de Examen"

    ws.append(["Nombre", "Descripción", "Activo"])
    for examen in TipoExamen.objects.all():
        ws.append([examen.nombre, examen.descripcion, "Sí" if examen.activo else "No"])

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return FileResponse(output, as_attachment=True, filename="tipos_examen.xlsx")
