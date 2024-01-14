from django.urls import path
<<<<<<< HEAD
from .views import profile_view, login_view, register_view, logout_view
=======
from .views import profile_view, login_view, register, logout_view
>>>>>>> origin/main

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
<<<<<<< HEAD
    path('register/', register_view, name='register'),
=======
    path('register/', register, name='register'),
>>>>>>> origin/main
    path('logout/', logout_view, name='logout'),
]