from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('signin', views.Signin.as_view(), name='signin'),
]
