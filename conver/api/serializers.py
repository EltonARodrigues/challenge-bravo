from rest_framework import serializers
from django.core.validators import RegexValidator
from conver.models import Currency

validator = [RegexValidator(regex='^.{3}$', message='Length has to be 3', code='nomatch')]


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ("__all__")

class CurrencyConversionSerializer(serializers.ModelSerializer):
    from_c = serializers.CharField(max_length=3,  validators=validator)
    to = serializers.CharField(max_length=3, validators=validator)
    amount = serializers.FloatField()

    class Meta:
        model = Currency
        fields = ('from_c', 'to', 'amount')

    def covert_curency(self):
        source_name =self.data['from_c']
        destination_name = self.data['to']
        value_to_convert = self.data['amount']

        try:
            source_value = self.__get_values_from_model(source_name)
            destination_value = self.__get_values_from_model(destination_name)
            result = (source_value / destination_value) * value_to_convert

        except Currency.DoesNotExist:
            result = 'Error to calculate... check the parameters'


        new_info ={ 'conversion ': result }
        new_info.update(self.data)

        return new_info

    def __get_values_from_model(self, name):
        return Currency.objects.values_list('coverage', flat=True).get(name=name)
