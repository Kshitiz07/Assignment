from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add_data,name="add")
]
