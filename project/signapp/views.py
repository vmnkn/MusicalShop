from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('musicshop:product_list')


@login_required
def become_manager(request):
    user = request.user
    if not request.user.groups.filter(name='manager').exists():
        mail_admins(
            subject=f'{user.username}: {user.email}',
            message=f'Пользователь {user.username} хочет стать менеджером.'
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
