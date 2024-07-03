from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import FormMixin

from main.forms import LinkForm, ContactForm
from main.models import Link, User
from django.views.generic.edit import ProcessFormView


class ContactFormView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverse_lazy('contact')
    extra_context = {'title': 'Связаться с нами'}

    def form_valid(self, form):
        return super().form_valid(form)


def home(request):
    return render(request, 'main/home.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

# def contact(request):
#     return render(request, 'main/contact.html', {'title': 'Связаться с нами'})


class LinksView(LoginRequiredMixin, FormView):
    template_name = 'main/links.html'
    form_class = LinkForm
    success_url = reverse_lazy('links')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['links'] = Link.objects.filter(user=current_user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


