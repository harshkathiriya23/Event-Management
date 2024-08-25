from django.urls import path
from .views import (
    register,
    login,
    insert_data,
    CheckLogin,
)

urlpatterns =[
    path('register', register ,name="register"),
    path('insert', insert_data ,name="insert"),
    path('login', login ,name="login"),
    path('Checklogin', CheckLogin ,name="checklogin"),
]
