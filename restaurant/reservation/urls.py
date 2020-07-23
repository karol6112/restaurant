from django.urls import path, include
from rest_framework import routers
from .views import ReservationViewSet

router = routers.DefaultRouter()
router.register(r'', ReservationViewSet, basename='reservation')


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
