from django.contrib.auth.decorators import permission_required

# Ya se usan decoradores en views.py como:
# @permission_required('examen.view_tipoexamen')
# Puedes definir permisos personalizados en Meta del modelo:
# class Meta:
#     permissions = [
#         ("can_export", "Puede exportar tipos de examen"),
#     ]
