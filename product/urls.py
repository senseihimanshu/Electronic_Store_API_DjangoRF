from django.urls import path, include

from rest_framework.routers import DefaultRouter

from product import views

router = DefaultRouter()
router.register('mobile', views.MobileViewSet)
router.register('laptop', views.LaptopViewSet)
router.register('', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]
