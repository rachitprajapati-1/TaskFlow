from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('todo/',views.todo,name='todo'),
    path('logout/', views.logout_view,name='logout'),
    path('add/',views.add_task,name='add_task')
]
