from django.shortcuts import get_object_or_404, render
from feincms3.applications import page_for_app_request

from .models import Article


def article_list(request):
    page = page_for_app_request(request)
    page.activate_language(request)
    articles = Article.objects.filter(is_active=True)
    return render(request, "blog/article_list.html", {"page": page, "articles": articles})


def article_detail(request, slug):
    page = page_for_app_request(request)
    page.activate_language(request)
    article = get_object_or_404(Article, slug=slug, is_active=True)
    return render(
        request,
        "blog/article_detail.html",
        {
            "page": page,
            "article": article,
            "regions": renderer.regions_from_item(article, timeout=60),
        },
    )