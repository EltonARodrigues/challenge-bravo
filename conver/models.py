from django.core.validators import RegexValidator
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True,
        validators=[RegexValidator(regex='^.{3}$', message='Length has to be 3', code='nomatch')])
    coverage = models.FloatField(null=False, blank=False)