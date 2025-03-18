from django.urls import path,include
from todo import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
]
