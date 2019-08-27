from django_filters.rest_framework import DjangoFilterBackend
from conver.helpers import ImportUSDFromExternalAPI
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import status

from .serializers import CurrencySerializer, CurrencyConversionSerializer
from conver.models import Currency
from django.http import JsonResponse



class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        data_from_api = False
        data = request.data

        name = str.upper(data['name'])
        converage = data['coverage']

        if self._verify_input(name, converage):

            external_api = ImportUSDFromExternalAPI()
            data_from_api = external_api.import_one(name)

        if data_from_api:
            serializer = self.get_serializer(data=data_from_api)
        else:
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _verify_input(self,name, coverage):
        return len(name) == 3 and coverage == ''

    @action(methods=['get'], detail=True)
    def import_all(self):

        external_api = ImportUSDFromExternalAPI()
        data_from_api = external_api.import_all()

        serialized = CurrencySerializer(data=data_from_api, many=True)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class CurrencyConversionView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencyConversionSerializer

    def get(self, request, *args, **kwargs):
        serializer = CurrencyConversionSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        value = serializer.covert_curency()

        return Response(value, status=status.HTTP_200_OK)


