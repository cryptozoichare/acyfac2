from django.utils.html import format_html, mark_safe
from feincms3.renderer import RegionRenderer

from .models import RichText, Image, Html

renderer = RegionRenderer()
renderer.register(RichText, lambda plugin, context: mark_safe(plugin.text))
renderer.register(
    Image,
    lambda plugin, context: format_html(
        '<figure><img src="{}" alt=""/><figcaption>{}</figcaption></figure>',
        plugin.image.url,
        plugin.caption,
    ),
)
renderer.register(Html, lambda plugin, context: mark_safe(plugin.html))