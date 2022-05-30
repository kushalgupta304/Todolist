from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView
from .models import Todo



# Create your views here.
def home_view(request):
    return render(request, 'todo/home.html')

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = "__all__"
    success_url= reverse_lazy('todo:list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url= reverse_lazy('todo:list')
