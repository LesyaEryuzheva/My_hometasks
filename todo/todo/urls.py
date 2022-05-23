from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='todo'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('baton/', include('baton.urls')),
]
