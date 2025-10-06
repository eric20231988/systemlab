def generar_pdf_analisis():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    # ... lógica actual ...
    p.save()
    buffer.seek(0)
    return buffer
