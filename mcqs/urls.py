from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^answer/$', views.answer, name='answer'),
] 
