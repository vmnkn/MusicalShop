from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from .models import Guitar, Basket
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
        context['basket'] = Basket.objects.filter(user=self.request.user)
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
    success_url = reverse_lazy('musicshop:guitar_list')


class GuitarUpdate(LoginRequiredMixin, UpdateView):
    model = Guitar
    template_name = 'guitar_update.html'
    form_class = GuitarForm


class GuitarDelete(LoginRequiredMixin, DeleteView):
    model = Guitar
    template_name = 'guitar_delete.html'
    success_url = reverse_lazy('')


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'account.html'


class BasketView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'basket.html'
    context_object_name = 'baskets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        total_quantity = 0
        total_sum = 0
        for basket in baskets:
            total_quantity += basket.quantity
            if basket.product.sale:
                total_sum += basket.sale_sum()
            else:
                total_sum += basket.sum()
        context['total_sum'] = total_sum
        context['total_quantity'] = total_quantity
        return context


def basket_add(request, product_id):
    page = request.META.get('HTTP_REFERER')
    product = Guitar.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(page)


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
