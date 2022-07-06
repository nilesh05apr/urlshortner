from rest_framework import serializers
from .models import URLS

class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URLS
        fields = ['id','short_url','long_url']