from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Guitar
from .filters import GuitarFilter
from .forms import GuitarForm
from django.http import HttpResponseRedirect


class GuitarList(ListView):
    model = Guitar
    ordering = 'price'
    template_name = 'guitars.html'
    context_object_name = 'guitars'
    paginate_by = 2  # кол-во товаров на 1 странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = GuitarFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale'] = None
        context['filterset'] = self.filterset
        return context


class GuitarDetailView(DetailView):
    model = Guitar
    template_name = 'guitar.html'
    context_object_name = 'guitar'


def guitar_create(request):
    form = GuitarForm()
    if request.method == 'POST':
        form = GuitarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('guitars')
    return render(request, 'guitar_create.html', {'form': form})
