from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment_dates/', views.payment_dates, name='payment_dates'),
    path('new_bill/', views.monthly_due, name='new_bill'),
]