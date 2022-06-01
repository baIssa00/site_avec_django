from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/new/', views.new_contact, name='new_contact'),
    path('contacts/edit/<int:id>/', views.edit_contact, name='edit_contact'),
    path('contacts/delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('contacts/<int:id>/', views.contact_details, name='contact_details'),
]