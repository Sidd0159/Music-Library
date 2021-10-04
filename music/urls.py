from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    
    path('',views.index, name='index'),

    path('register/',views.register, name='register'),

    path('login_user/', views.login_user, name='login_user'),

    path('logout_user/', views.logout_user, name='logout_user'),

    path('<album_id>[0-9]+/', views.detail, name='detail'),

    path('<album_id>/fav_song/<song_id>/', views.favorite, name='favorite'),

    path('songs/<filter_by>[a-zA_Z]+', views.songs, name='songs'),

    path('album_add/', views.create_album ,name='create_album'),

    path('<album_id>/add_song/', views.create_song, name='create_song'),

    path('<album_id>/delete_song/<song_id>/', views.delete_song, name='delete_song'),

    path('<album_id>/favo_alb/', views.favorite_album, name='favorite_album'),

    path('album/<album_id>/delete_album',views.delete_album,name='delete_album'),

]