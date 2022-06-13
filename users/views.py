from django.http import JsonResponse, HttpResponse
from .models import User, User_child
from .serializers import UserSerializer, User_child_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        # get all users
        # serialize them
        # return a json response
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse({"users": serializer.data})
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def user_child_list(request):

    if request.method == 'GET':
        # get all child
        # serialize them
        # return json response
        user_child = User_child.objects.all()
        serializer = User_child_serializer(user_child, many=True)
        return JsonResponse({"Child": serializer.data})
    if request.method == 'POST':
        serializer = User_child_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_child_detail(request, id):
    try:
        child = User_child.objects.get(pk=id)
    except User_child.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = User_child_serializer(child)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = User_child_serializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)