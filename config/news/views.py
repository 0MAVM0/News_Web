from django.shortcuts import render
from .models import *

def home_page(request):
    a_piece_of_news = News.published.order_by("-id").first()
    latest = News.published.order_by("-id")[:5]
    sports_news = News.published.filter(category__name="Sports")
    technologies_news = News.published.filter(category__name="Technologies")
    local_news = News.published.filter(category__name="Local")
    overseas_news = News.published.filter(category__name="Overseas")

    context = {
        "a_piece_of_news" : a_piece_of_news,
        "latest" : latest,
        "sports" : sports_news,
        "technologies" : technologies_news,
        "local" : local_news,
        "overseas" : overseas_news,
    }

    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def single_page(request, slug):
    news = News.objects.filter(slug=slug).first()
    context = { "a_piece_of_news" : news}

    return render(request, "single-page.html", context)

def sports_news(request):
    sports_news = News.objects.filter(category__name="Sports")
    context = { "sports" : sports_news }

    return render(request, "sports.html", context)

def technology_news(request):
    sports_news = News.objects.filter(category__name="Technologies")
    context = { "technologies" : sports_news }

    return render(request, "technologies.html", context)

def local_news(request):
    sports_news = News.objects.filter(category__name="Local")
    context = { "local_news" : sports_news }

    return render(request, "local.html", context)

def overseas_news(request):
    sports_news = News.objects.filter(category__name="Overseas")
    context = { "overseas_news" : sports_news }

    return render(request, "overseas.html", context)
