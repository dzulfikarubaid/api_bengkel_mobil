from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer, ServisSerializer
from .models import ServisModel

# Create your views here.
def index(request):
    return redirect('docs/')
@api_view(['POST'])
def add_servis(request):
    serializer = ServisSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    if user.is_authenticated:
        serializer.save()
        return Response({
            'nomor antrian':serializer.data['id'],
            'username':user.username,
            'waktu pengajuan':serializer.data['dibuat_pada'],
            'keluhan':serializer.data['keluhan']
        })
    return Response({
        'error':'not authenticated'
    }, status=400)
@api_view(['GET'])
def servis_list(request):
    ServisObj=ServisModel.objects.all()
    ServisSerializeObj = ServisSerializer(ServisObj,many=True)
    return Response(ServisSerializeObj.data)

@api_view(['POST'])
def update_servis(request,pk):
    user = request.user
    if user.is_authenticated:
        try:
            ServisObj=ServisModel.objects.get(pk=pk)
        except:
            return Response("Data not found")
        serializeObj = ServisSerializer(ServisObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)
    return Response({
        'error':'not authenticated'
    }, status=400)

@api_view(['POST'])
def delete_servis(request,pk):
    user = request.user
    if user.is_authenticated:
        try:
            ServisObj=ServisModel.objects.get(pk=pk)
        except:
            return Response("Data not found")
        ServisObj.delete()
        return Response(200)
    return Response({
        'error':'not authenticated'
    }, status=400)

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })
@api_view(['GET'])
def user_list(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            }
        })
    return Response({
        'error':'not authenticated'
    }, status=400)


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })