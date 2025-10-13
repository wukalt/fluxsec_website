import requests
from django.views.generic import TemplateView, DetailView, ListView
from .models import News

class HomeView(TemplateView):
    template_name = 'home.html'


class PrivacyView(TemplateView):
    template_name = 'privacy.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class NewsView(ListView):
    model = News
    template_name = 'news.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
