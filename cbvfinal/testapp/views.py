from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Bear

# Create your views here.
class BearListView(ListView):
    model=Bear


class BearDetailView(DetailView):
    model=Bear

class BearCreateView(CreateView):
    model=Bear
    fields="__all__"

class BearUpdateView(UpdateView):
    model=Bear
    fields=['price',]

from django.urls import reverse_lazy
class BearDeleteView(DeleteView):
    model=Bear
    success_url=reverse_lazy('list')
