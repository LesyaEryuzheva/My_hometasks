from rest_framework import routers

from .views import CartViewSet

router = routers.DefaultRouter()
router.register('', CartViewSet, basename='carts')

urlpatterns = router.urls
