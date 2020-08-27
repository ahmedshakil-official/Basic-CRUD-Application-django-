
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_musician/', views.add_musician, name='add_musician'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('update_artist/<int:artist_id>/', views.update_artist, name='update_artist'),
    path('update_album/<int:album_id>/', views.update_album, name='update_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]