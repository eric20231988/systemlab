from django.http import FileResponse
from ..services.export import generar_pdf_analisis, generar_excel_perfiles

def exportar_analisis_pdf(request):
    buffer = generar_pdf_analisis()
    return FileResponse(buffer, as_attachment=True, filename="analisis_labmedic.pdf")

def exportar_perfiles_excel(request):
    buffer = generar_excel_perfiles()
    return FileResponse(buffer, as_attachment=True, filename="perfiles_labmedic.xlsx")
