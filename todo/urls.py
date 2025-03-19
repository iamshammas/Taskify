from django.urls import path,include
from todo import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('loginn',views.loginn,name='loginn'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('add_task',views.add_task,name='add_task'),
]
