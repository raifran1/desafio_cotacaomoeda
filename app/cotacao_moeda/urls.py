from django.urls import path
from .views import update_coins_cotation


urlpatterns = [
    path('update-cotation/', update_coins_cotation, name='update_coins_cotation'),
]
