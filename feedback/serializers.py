__author__ = 'Pavan Kotehal'

from . import models
from rest_framework import serializers


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'user': {'write_only': True}
        }
        fields = (
            'id',
            'survey',
            'question',
            'answer',
            'user',
        )
        model = models.Response

