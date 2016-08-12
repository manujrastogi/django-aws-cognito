from django.views.generic.base import TemplateView
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),

]