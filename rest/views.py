from django.http import response
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import ArtistSerializer, AlbumSerializer, MusicSerializer
from .models import Artist, Music, Album
from rest import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
#from rest_framework.authentication.permisssions import CustomObjectPermissions, IsOwner
from rest_framework import permissions
from django.core.paginator import Paginator
from rest_framework_datatables.pagination import DatatablesPageNumberPagination
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

class X(DatatablesPageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class APIGET(ModelViewSet):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    pagination_class = X
    serializer_class= MusicSerializer
    queryset=Music.objects.all()

    def create(self, request):
        response = {'message': 'Damini OL'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        response = {'message': 'Damini OL'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Damini OL.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Damini OL'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class ArtistGetListView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(instance=queryset, many=True)
        #return Response(serializer.data)
        page_number = self.request.query_params.get('page_number ', 1)
        page_size = self.request.query_params.get('page_size ', 10)

        paginator = Paginator(queryset , page_size)
        serializer = ArtistSerializer(paginator.page(page_number) , many=True, context={'request':request})
        # -----------------------------------------------------------

        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response
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
