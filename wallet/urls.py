from django.urls import path
from .views import list_account,account_profile,register_customer,customer_profile,list_customer,home

urlpatterns = [
    path("", home, name="home"),  # <-- NEW
    path("accounts/", list_account, name="list_account"),
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("register/", register_customer, name="register_customer"),
    path("customers/<int:id>/",customer_profile,name="customer_profile"),
    path("customers/",list_customer,name="customer_list"),

]
