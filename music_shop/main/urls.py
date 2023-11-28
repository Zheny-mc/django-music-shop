from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    BaseView,
    AboutView,
    ArtistDetailView,
    AlbumDetailView,
    AccountView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    # path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    # path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail'),
    # для корзины
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty')
]
