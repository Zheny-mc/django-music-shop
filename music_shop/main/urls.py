from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import RegistrationView, LoginView, BaseView, AboutView
from .views import ArtistDetailView, AlbumDetailView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
