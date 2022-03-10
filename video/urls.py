from django.urls import path
from . import views


urlpatterns = [
    path('', views.all, name='index'),
    path('<int:pk>', views.detail, name='movie'),
    path('search/', views.search, name='search'),
    path('genres/<int:pk>', views.genres, name='genres'),
]