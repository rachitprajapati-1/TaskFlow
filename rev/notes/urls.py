from django.urls import path
from . import views
app_name='notes'
urlpatterns=[
    path('', views.notes_list, name='list'),
    path('add/', views.add_note, name='add'),
    path('edit/<int:id>/',views.edit_note,name='edit'),
    path('delete/<int:id>/', views.delete_note, name='delete'),
]