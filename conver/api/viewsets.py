from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from conver.models import Currency
from .serializers import CurrencySerializer, CurrencyConversionSerializer
from rest_framework.response import Response
from rest_framework import status

import django_filters.rest_framework
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyConversionView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencyConversionSerializer

    def get(self, request, *args, **kwargs):
        serializer = CurrencyConversionSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        value = serializer.covert_curency()

        return Response(value, status=status.HTTP_200_OK)
