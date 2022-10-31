from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('make_order/', views.MakeOrderView, name='make_order')]