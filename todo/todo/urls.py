from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='todo'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('baton/', include('baton.urls')),
]
