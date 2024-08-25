from django.urls import path
from .views import (
    register, 
    insert_data,
)

urlpatterns =[
    path('register', register ,name="register"),
    path('insert', insert_data ,name="insert"),
]
