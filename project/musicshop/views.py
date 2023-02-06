from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from .models import Guitar
from .filters import GuitarFilter
from .forms import GuitarForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class GuitarList(LoginRequiredMixin, ListView):
    model = Guitar
    ordering = 'price'
    template_name = 'guitars.html'
    context_object_name = 'guitars'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = GuitarFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale'] = None
        context['filterset'] = self.filterset
        return context


class GuitarSearch(GuitarList):
    template_name = 'guitar_search.html'


class GuitarDetailView(LoginRequiredMixin, DetailView):
    model = Guitar
    template_name = 'guitar.html'
    context_object_name = 'guitar'


class GuitarCreate(LoginRequiredMixin, CreateView):
    model = Guitar
    template_name = 'guitar_create.html'
    form_class = GuitarForm


class GuitarUpdate(LoginRequiredMixin, UpdateView):
    model = Guitar
    template_name = 'guitar_create.html'
    form_class = GuitarForm


class GuitarDelete(LoginRequiredMixin, DeleteView):
    model = Guitar
    template_name = 'guitar_delete.html'
    success_url = reverse_lazy('')


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'account.html'
