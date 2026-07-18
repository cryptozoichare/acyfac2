from content_editor.admin import ContentEditor
from django.contrib import admin
from feincms3.plugins import image, richtext

from . import models


@admin.register(models.Article)
class ArticleAdmin(ContentEditor):
    list_display = ["title", "is_active", "publication_date"]
    list_editable = ["is_active"]
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        richtext.RichTextInline.create(model=models.RichText),
        image.ImageInline.create(model=models.Image),
    ]