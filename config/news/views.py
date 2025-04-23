from django.shortcuts import render
from .models import *

def home_page(request):
    latest_news = News.published.order_by("-id").first()
    context = { "latest_news" : latest_news }

    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def single_page(request):
    return render(request, "single-page.html")
