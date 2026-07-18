from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from content_editor.models import Region, create_plugin_base
from django_prose_editor.fields import ProseEditorField
from feincms3 import plugins
from feincms3.applications import reverse_app


class Article(models.Model):
    is_active = models.BooleanField(_("is active"), default=False)
    title = models.CharField(_("title"), max_length=200)
    slug = models.SlugField(_("slug"), unique_for_year="publication_date")
    publication_date = models.DateTimeField(_("publication date"), default=timezone.now)

    regions = [Region(key="main", title=_("Main"))]

    class Meta:
        ordering = ["-publication_date"]
        get_latest_by = "publication_date"
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_app(
            "blog",
            "article-detail",
            kwargs={"year": self.publication_date.year, "slug": self.slug},
        )


ArticlePlugin = create_plugin_base(Article)


class RichText(plugins.richtext.RichText, ArticlePlugin):
    text = ProseEditorField(
        extensions={
            "Bold": True,
            "Italic": True,
            "ListItem": True,
            "BulletList": True,
            "OrderedList": True,
            "Link": True,
            "Blockquote": True,
            "CodeBlock": True,
            "Code": True,
        },
        sanitize=True,
    )


class Image(plugins.image.Image, ArticlePlugin):
    pass

class Html(plugins.html.HTML, ArticlePlugin):
    pass