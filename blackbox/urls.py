from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fines', views.fines, name='fines'),
    path('users', views.users, name='users'),
    path('users/<int:user_id>/payment', views.payment, name='payment'),
]
