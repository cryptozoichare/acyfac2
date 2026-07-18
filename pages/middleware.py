from django.shortcuts import render

from .models import Page
from .renderer import page_context


def page_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code != 404:
            # Someone else already handled this request
            return response

        # path is the full path, path_info excludes the script prefix.
        if page := Page.objects.active().filter(path=request.path_info).first():
            return render(
                request,
                "pages/standard.html",
                page_context(request, page=page),
            )

        # No page found, fall back to the original 404 response
        return response

    return middleware