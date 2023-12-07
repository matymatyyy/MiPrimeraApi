from rest_framework import routers
from .api import ProductosViewSets


router = routers.DefaultRouter()

router.register("api/productos", ProductosViewSets, "productos")

urlpatterns = router.urls
