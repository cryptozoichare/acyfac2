from django.shortcuts import get_object_or_404
from feincms3.applications import page_for_app_request
from feincms3.shortcuts import render_list, render_detail

from pages.renderer import renderer as page_renderer

from .models import Article
from .renderer import renderer as article_renderer


def article_list(request):
    page = page_for_app_request(request)
    return render_list(
        request,
        Article.objects.filter(is_active=True),
        {
            "page": page,
            "page_regions": page_renderer.regions_from_item(page, timeout=30),
        },
        paginate_by=10,
    )


def article_detail(request, year, slug):
    page = page_for_app_request(request)
    article = get_object_or_404(
        Article.objects.filter(is_active=True),
        publication_date__year=year,
        slug=slug,
    )
    return render_detail(
        request,
        article,
        {
            "page": page,
            "content_regions": article_renderer.regions_from_item(article, timeout=30),
        },
    )