from django.urls import path
from . import views

app_name='myapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('todo/',views.todo,name='todo'),
    path('logout/', views.logout_view,name='logout'),
    path('add/',views.add_task,name='add_task'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('update/<int:id>/',views.update_task,name='update_task'),
    path('update_status/<int:id>',views.update_status,name='update_status'),
]
