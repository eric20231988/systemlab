from rest_framework.routers import DefaultRouter
from .views import TipoExamenViewSet

router = DefaultRouter()
router.register(r'tipos-examen', TipoExamenViewSet)

urlpatterns = router.urls
