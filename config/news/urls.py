from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("contact_page/", contact, name="contact"),
    # path("single_page/", single_page, name="single_page"),
]
