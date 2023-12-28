from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main import models
from main.models import MediaType, Genre, Member, Artist, Album, Cart, Customer, CartProduct

# Create your tests here.
class BaseTest(TestCase):
    def setUp(self):
        """Инициализация тестовой Базы данных"""
        self.register_url = reverse('registration')
        self.user = {
            'email': "test@gmail.com",
            'username': "username",
            'password': "password",
            'confirm_password': "password",
            'first_name': "first_name",
            'last_name': "last_name",
            'phone': '+79999999999',
            'address': 'адрес'
        }
        member = Member(name='member 1', slug='member-1', image='')
        member.save()
        genre = Genre(name='jaze', slug='jaze')
        genre.save()
        artist = Artist(name='group 1', slug='group-1', image='', genre=genre)
        artist.save()
        artist.members.set([member])

        media_type = MediaType(name='пластинка')
        media_type.save()
        self.album = Album(artist=artist, name='album 1', media_type=media_type, songs_list='',
                      release_date=datetime.now(), slug='album-1', price=100, image='')
        self.album.save()
        return super().setUp()
class RegisterTest(BaseTest):
    def test_can_register_user(self):
        """Проверка доступа к регистрации"""
        responce = self.client.get(self.register_url)
        self.assertEquals(responce.status_code, 200)

    def test_register_user(self):
        """проверка регистрации пользователя"""
        responce = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEquals(responce.status_code, 302)
        user = User.objects.get(username='username')
        self.assertTrue(user)

class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.client.post(self.register_url, self.user, format='text/html')

    def test_login_user(self):
        """Тест на вход"""
        login = self.client.login(username="username", password="password")
        self.assertTrue(login)

    def test_get_account(self):
        """Тест на полчение личного кабинета"""
        login = self.client.login(username="username", password="password")
        self.assertTrue(login)
        responce = self.client.get(reverse('account'))
        self.assertEquals(responce.status_code, 200)

class CartTest(BaseTest):
    def setUp(self):
        '''инииализация'''
        super().setUp()
        self.client.post(self.register_url, self.user, format='text/html')
        login = self.client.login(username="username", password="password")
        self.assertTrue(login)
        customer = Customer.objects.get(user=User.objects.get(username='username'))
        self.cart = Cart.objects.create(owner=customer)
        self.cart.save()

    def test_add_album(self):
        """Проверка добавления товара в корзину"""
        responce = self.client.get(f'/add-to-cart/album/{self.album.slug}/')
        self.assertEquals(responce.status_code, 302)
        self.assertEquals(len(self.cart.products_in_cart()), 1)

    def test_delete_album(self):
        """Проверка удаления товара в корзину"""
        self.client.get(f'/add-to-cart/album/{self.album.slug}/')
        self.assertEquals(len(self.cart.products_in_cart()), 1)
        responce = self.client.get(f'/remove-from-cart/album/{self.album.slug}/')
        self.assertEquals(responce.status_code, 302)
        self.assertEquals(len(self.cart.products_in_cart()), 0)

    def test_change_count(self):
        """Проверка изменения товара в корзине"""
        self.client.get(f'/add-to-cart/album/{self.album.slug}/')
        self.assertEquals(self.cart.products.all()[0].qty, 1)
        responce = self.client.post(f'/change-qty/album/{self.album.slug}/', {'qty': 2})
        self.assertEquals(responce.status_code, 302)
        self.assertEquals(self.cart.products.all()[0].qty, 2)