from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return redirect("contact")

    return render(request, "contact.html")

def single_page(request, slug):
    news = News.objects.filter(slug=slug).first()
    all_comments = Comment.objects.filter(news=news, status=True).order_by("-created_at")
    news.count += 1
    news.save()
 
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        message = request.POST.get("message")

        if message:
            comment = Comment(user=request.user, comment=message, news=news)
            comment.save()

            return redirect("single_page", slug=slug)

    context = {
        "a_piece_of_news" : news,
        "all_comments": all_comments,
    }

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

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/registrate.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = "user/login.html"

def log_out(request):
    if request.method == "POST":
        logout(request)

        return redirect("home")
    return render(request, "user/logout.html")
