from django.shortcuts import render
from .models import News


def index(request):
    news_list = News.objects.all()
    context = {'news':news_list}
    return render(request, 'news/base_news.html', context)

# Create your views here.
