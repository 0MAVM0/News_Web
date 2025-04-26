from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("contact_page/", contact, name="contact"),
    path("detail_page/<int:id>", single_page, name="single_page"),
]
