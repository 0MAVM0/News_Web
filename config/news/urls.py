from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("contact_page/", contact, name="contact"),
    path("detail_of/<slug:slug>/", single_page, name="single_page"),
    path("sport/", sports_news, name="sports"),
    path("technology/", technology_news, name="technology"),
    path("local/", local_news, name="local"),
    path("overseas/", overseas_news, name="overseas"),
    path("registrate/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", log_out, name="logout"),
]
