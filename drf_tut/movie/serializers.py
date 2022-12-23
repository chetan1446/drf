from collections import UserDict
from typing import Collection
from django.db import models
from django.db.models import fields
from .models import MovieBank
from rest_framework import serializers
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieBank
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'