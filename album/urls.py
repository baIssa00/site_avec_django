from django.urls import path

from . import views

urlpatterns = [
    path('album/', views.album, name='album'),
    path('album/new_photo/', views.new_photo, name='new_photo'),
]
