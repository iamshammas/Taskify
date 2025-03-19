from django.urls import path,include
from todo import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('loginn',views.loginn,name='loginn'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_task',views.add_task,name='add_task'),
    path('update_task/<int:pk>',views.update_task,name='update_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('logout_user',views.logout_user,name='logout_user'),
]
