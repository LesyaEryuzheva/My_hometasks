from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_brand, name='cars'),
    path('model', views.create_car_model, name='model'),
    path('engine', views.create_engine, name='engine'),
]
