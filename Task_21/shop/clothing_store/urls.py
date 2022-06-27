from rest_framework import routers

from .views import BrandViewSet, ClothingViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register('brand', BrandViewSet, basename='brand')
router.register('clothing', ClothingViewSet, basename='clothing')
router.register('item', ItemViewSet, basename='item')

urlpatterns = router.urls
