from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wangges.serializers import UserSerializer, GroupSerializer
from wangges.models import Stockcode as SC
from wangges.serializers import StockcodeSerializer
from wangges.models import ZXG
from wangges.serializers import ZXGSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET', 'POST'])
def stockcode_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        values = SC.objects.all()
        serializer = StockcodeSerializer(values, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockcodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stockcode_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        values = SC.objects.get(pk=pk)
    except SC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockcodeSerializer(values)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockcodeSerializer(values, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        values.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ZXG_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        values = ZXG.objects.all()
        serializer = ZXGSerializer(values, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ZXGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ZXG_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        values = ZXG.objects.get(pk=pk)
    except SC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ZXGSerializer(values)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ZXGSerializer(values, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        values.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
