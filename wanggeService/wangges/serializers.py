# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : serializers.py.py
Description :
@Author :       pchaos
date：          18-4-3
-------------------------------------------------
Change Activity:
               18-4-3:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from wangges.models import Stockcode

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StockcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stockcode
        fields = ('code', 'name', 'market', 'isindex')