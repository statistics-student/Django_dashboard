from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('mch',views.mch,name='mch'),
    path('xjs',views.xjs,name='xjs'),
    path('sxh',views.sxh,name='sxh'),
    path('tty',views.tty,name='tty'),
    path('base',views.base,name='base'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]