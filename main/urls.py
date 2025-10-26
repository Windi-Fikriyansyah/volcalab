from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funfact/', views.funfact, name='funfact'),
    path('wahkokbisa/', views.wahkokbisa, name='wahkokbisa'),
    path('howtouse/', views.howtouse, name='howtouse'),
    path('product/', views.product, name='product'),
]
