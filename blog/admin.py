from django.contrib import admin
from content_editor.admin import ContentEditor
from feincms3 import plugins

from . import models


@admin.register(models.Article)
class ArticleAdmin(ContentEditor):
    date_hierarchy = "publication_date"
    list_display = ["title", "is_active", "publication_date"]
    list_editable = ["is_active"]
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        plugins.richtext.RichTextInline.create(models.RichText),
        plugins.image.ImageInline.create(models.Image),
        plugins.html.HTMLInline.create(models.Html),
    ]