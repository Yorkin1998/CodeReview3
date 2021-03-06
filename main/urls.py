"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Api-Get', views.APIGET)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get', include(router.urls)),
    path('api/artist-get',views.ArtistGetListView.as_view()),
    path('api/artist-get/<int:pk>',views.ArtistDetialView.as_view()),
    path('chaining/', include('smart_selects.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
