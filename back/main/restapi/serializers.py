from rest_framework import serializers
from dataclasses import field
from ..models import *

class serializer_User(serializers.ModelSerializer):
    class Meta:
        model = model_User
        fields = '__all__'

class serializer_SmallTask(serializers.ModelSerializer):
    class Meta:
        model = model_SmallTask
        fields = '__all__'
