from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/login/', views.obtain_auth_token),
    path('api/users/', include('accounts.urls')),
    path('api/movies/', include('movies.urls')),
]
