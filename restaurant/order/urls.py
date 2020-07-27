from django.urls import path, include
from rest_framework import routers
from .views import PositionViewSet, OrderViewSet, BillViewSet

router = routers.DefaultRouter()
router.register(r'menu', PositionViewSet, basename='menu')
router.register(r'bill', BillViewSet, basename='bill')
router.register(r'', OrderViewSet, basename='order')


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
