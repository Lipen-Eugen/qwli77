from django.urls import path
from .views import *


app_name='mytest'
urlpatterns = [

    path('',map,name='map'),
    path('out/',OutDB.as_view(),name='out'),
    path('in/', point_input, name='in'),
    path('outmap/',Outmap.as_view(),name='outmap'),

]