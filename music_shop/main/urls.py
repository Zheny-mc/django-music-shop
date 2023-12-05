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
    ChangeQTYView,
    AddToWishlistView,
    ClearNotificationsViews,
    RemoveFromWishListView
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    # лист ожидания
    path('add-to-wishlist/<int:album_id>', AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('remove-from-wishlist/<int:album_id>', RemoveFromWishListView.as_view(), name='remove_from_wishlist'),
    # для корзины
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('clear-notifications/', ClearNotificationsViews.as_view(), name='clear-notifications'),
    # получение модели
    path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail'),
]
