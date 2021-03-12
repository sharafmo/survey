from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('assign_name', views.submission),
    path('result', views.result)
]

