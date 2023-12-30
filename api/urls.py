from django.urls import path,include
from .views import *

urlpatterns = [
    path('', Homepage.as_view(),name='Homepage'),
    path('items/<int:id>', Singleproduct.as_view(),name='Singleproduct'),
    path('purchase/', Purchase_page,name='Purchase_page'),
    path('purchase-history/', Purchase_History,name='Purchase_History'),
]
