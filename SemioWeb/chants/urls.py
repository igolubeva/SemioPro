from django.urls import path
from chants import views

urlpatterns = [
    path('krug/<int:year>/', views.krug_glas, name='krug_chant'),
    path('krug/', views.krug_glas, name='krug_chant'),
              ]

