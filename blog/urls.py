from django.urls import path, re_path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.article_list, name="article-list"),
    re_path(r"^(?P<year>\d{4})/(?P<slug>[-\w]+)/$", views.article_detail, name="article-detail"),
]