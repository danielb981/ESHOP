from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import NEW

def news_list(request):
    news = NEW.objects.all()
    return render(request, 'news.html', {'news': news})