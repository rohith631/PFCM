from django.urls import path
from .views import mad, mad1,mad2,mad3,mad4,mad5,mad6,mad7


urlpatterns = [
    path('', mad, name='home'),
    path('admin/', mad1, name='admin'),
    path('transaction/', mad2, name='transactions'),
    path('newtospeedo/', mad6, name='new to speedo'),
    path('order/', mad5, name='order'),
    path('shipping/', mad4, name='shipping'),
    path('tracking/', mad3, name='tracking'),
    path('delivery/', mad7, name='delivery'),

]
