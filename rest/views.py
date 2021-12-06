from django.http import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ArtistSerializer, AlbumSerializer, MusicSerializer
from .models import Artist, Music, Album
from rest import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
#from rest_framework.authentication.permisssions import CustomObjectPermissions, IsOwner
from rest_framework import permissions


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    
    #edit_methods = ("PUT", "PATCH")
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
    # def has_object_permission(self, request, view, obj):
    #     print(request.user.is_superuser)
    #     if request.user.is_superuser:
    #         return True
    #     else:
    #         False
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # if obj.author == request.user:
        #     return True

        # if request.user.is_staff and request.method not in self.edit_methods:
        #     return False

        # return False

class APIGET(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def get(self, request):
        queryset = Music.objects.all()
        serializer = MusicSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class ArtistGetListView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ArtistDetialView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]

    def get(self, request, pk):
        queryset = Artist.objects.get(id=pk)
        serializer = ArtistSerializer(instance=queryset, many=False)
        return Response(serializer.data)

    def put(self,request,pk):
        queryset=Artist.objects.get(id=pk)
        serializer = ArtistSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = Artist.objects.get(id=pk)
        queryset.delete()
        return Response("Successfully deleted")
