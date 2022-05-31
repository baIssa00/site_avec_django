from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact_list, name='contact_list'),
    # ex: /contact/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('contacts/<int:id>/', views.contact_details, name='contact_details'),
]