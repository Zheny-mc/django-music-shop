from django.shortcuts import render
from django import views
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .mixins import CartMixin
from .models import Customer, Artist, Album
from .forms import LoginForm, RegistrationForm


class BaseView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html', {})

class AboutView(views.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main/about.html', {})


class ArtistDetailView(views.generic.DetailView):
    model = Artist
    template_name = 'main/artist/artist_detail.html'
    slug_url_kwarg = 'artist_slug'
    context_object_name = 'artist'

class AlbumDetailView(views.generic.DetailView):
    model = Album
    template_name = 'main/album/album_detail.html'
    slug_url_kwarg = 'album_slug'
    context_object_name = 'album'

class LoginView(views.View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'main/login.html', context)

class RegistrationView(views.View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)


    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'main/registration.html', context)

class AccountView(CartMixin, views.View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        context = {
            'customer': customer,
            'cart': self.cart
        }
        return render(request, 'main/accounts.html', context)





















