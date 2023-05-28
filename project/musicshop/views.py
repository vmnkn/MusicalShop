from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from .models import Basket, Product, Category
from .filters import ProductFilter
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins, mail_managers


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    ordering = 'name'
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 4
    login_url = reverse_lazy('login')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


class StringsList(LoginRequiredMixin, ListView):
    model = Product
    ordering = 'price'
    template_name = 'product/strings.html'
    context_object_name = 'strings'
    paginate_by = 4
    queryset = Product.objects.all().filter(category__name='Струны')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


class GuitarsList(LoginRequiredMixin, ListView):
    model = Product
    ordering = 'price'
    template_name = 'product/guitars.html'
    context_object_name = 'guitars'
    paginate_by = 4
    queryset = Product.objects.all().filter(category__name='Гитары')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


class KombosList(LoginRequiredMixin, ListView):
    model = Product
    ordering = 'price'
    template_name = 'product/kombos.html'
    context_object_name = 'kombos'
    paginate_by = 4
    queryset = Product.objects.all().filter(category__name='Комбоусилители')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


class PedalsList(LoginRequiredMixin, ListView):
    model = Product
    ordering = 'price'
    template_name = 'product/pedals.html'
    context_object_name = 'pedals'
    paginate_by = 4
    queryset = Product.objects.all().filter(category__name='Педали')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


class ProductSearch(ProductList):
    template_name = 'product/product_search.html'
    paginate_by = 2


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_manager'] = self.request.user.groups.filter(name='manager').exists()
        return context


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('musicshop:product_list')
    permission_required = ('musicshop.add_product', )


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('musicshop:product_list')
    permission_required = ('musicshop.change_product',)


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('musicshop:product_list')
    permission_required = ('musicshop.delete_product',)


class UserView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_manager'] = not self.request.user.groups.filter(name='manager').exists()
        context['is_manager'] = self.request.user.groups.filter(name='manager').exists()
        return context


class BasketView(LoginRequiredMixin, ListView):
    model = Basket
    template_name = 'basket.html'
    context_object_name = 'baskets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        total_quantity = 0
        total_sum = 0
        for basket in context['baskets']:
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
    product = Product.objects.get(id=product_id)
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


@login_required
def make_order(request):
    user = request.user
    total_quantity = 0
    total_sum = 0
    for basket in Basket.objects.filter(user=request.user):
        total_quantity += basket.quantity
        if basket.product.sale:
            total_sum += basket.sale_sum()
        else:
            total_sum += basket.sum()
    mail_admins(
        subject=f'{user.username}: {user.email}',
        message=f'Пользователь {user.username} сделал заказ - всего товаров: {total_quantity}, общая цена: {total_sum}'
    )

    mail_managers(
        subject=f'{user.username}: {user.email}',
        message=f'Пользователь {user.username} сделал заказ - всего товаров: {total_quantity}, общая цена: {total_sum}'
    )
    return HttpResponseRedirect('http://127.0.0.1:8000/shop/order/')


class OrderView(BasketView):
    template_name = 'order.html'
