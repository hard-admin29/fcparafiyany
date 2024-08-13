from django.shortcuts import render, redirect
from .models import ModelNews
from .forms import MediaForm


def news(request) -> render:
    news_from_bd = ModelNews.objects.order_by("-data")
    return render(request, "news/index.html", {"news": news_from_bd})


def create_new(request) -> render:
    error = ""
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Не правильно заповнена форма"
    form = MediaForm()

    data = {
        "form": form,
        "error": error
    }

    return render(request, "news/create_news.html", data)

