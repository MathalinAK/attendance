

from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    loginView,registerprocessView,homeView,ListView,logoutView,
   
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView.as_view(), name='login'), 
    path('registerprocess/', registerprocessView.as_view(), name='registerprocess'), 
    path('home/',homeView.as_view(),name='home'),
    path('list/',ListView.as_view(),name='list'),
    path('logout/',logoutView.as_view(),name='logout'),
    
]