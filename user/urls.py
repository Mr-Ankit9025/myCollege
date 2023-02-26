from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('aboutus/',views.aboutus),
    path('courses/',views.courses),
    path('register/',views.register),
    path('contactus/',views.contactus),
    path('gallery/',views.gallery),
    path('login/',views.login),
    path('infra/',views.infra),
    path('facualty/',views.facualty),

    path('placement/',views.placement),
    path('video/',views.vdogallery),
    path('details/',views.vdodetails),



]