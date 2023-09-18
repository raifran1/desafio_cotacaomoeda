from api.views import QuotationCoinViewSet, CoinsViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register('quotationcoin-graphic', QuotationCoinViewSet, 'quotationcoin')
router.register('coins', CoinsViewSet, 'CoinsViewSet')

urlpatterns = [] + router.urls
