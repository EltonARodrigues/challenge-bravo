from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from conver.api.viewsets import CurrencyViewSet
from conver.api.viewsets import CurrencyConversionView

router = routers.DefaultRouter()
router.register(r'currency', CurrencyViewSet)
#router.register(r'convert', CurrencyConversionViewSet)


urlpatterns = [
    path('import_all/',CurrencyViewSet.import_all, name='detail'),
    path('convert/', CurrencyConversionView.as_view(), name="currency"),
    path('', include(router.urls))
]
