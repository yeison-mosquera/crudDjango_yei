from django.url import path, include
from rest_framework.routers import DefaultRouter
from api_views import clienteviwset

router = DefaultRouter()
router.register(r'clientes', clienteviwset)

urlpatterns = [
    path('', include(router.urls)),
]