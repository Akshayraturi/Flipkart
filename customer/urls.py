
from django.urls import path,include
from customer.views import*
urlpatterns = [
    path('get-customers',GetcustomerViews.as_view()),
    path('get-customer-address',GetCustomersAddressViews.as_view()),
 
]