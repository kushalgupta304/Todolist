from django.urls import path
from .import views

app_name = 'todo'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('list', views.TodoListView.as_view(),name='list'),
    path('create/', views.TodoCreateView.as_view(),name='create'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(),name='delete'),

]
