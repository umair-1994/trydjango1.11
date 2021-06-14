from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import ItemForm

# Create your views here.


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):
    success_url = 'www.google.com/'
    form_class = ItemForm
    template_name = 'form.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Item'
        return context


class ItemUpdateView(UpdateView):
    success_url = 'www.google.com/'
    template_name = 'form.html'
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context
