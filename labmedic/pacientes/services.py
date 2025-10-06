# pacientes/services.py
def crear_paciente(form):
    return form.save(commit=True)

def actualizar_paciente(form):
    return form.save(commit=True)

def eliminar_paciente(paciente):
    paciente.delete()
    return True
