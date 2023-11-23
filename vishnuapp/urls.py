from django.urls import path
from vishnuapp import views

urlpatterns = [
    path('',views.index),
    path('index1/',views.index1),
]