from rest_framework import serializers
from app.models import *


class IplModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ipl
        #fields='__all__'
        fields=['Tname']