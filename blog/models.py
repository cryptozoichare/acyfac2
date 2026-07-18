from content_editor.models import Region, create_plugin_base
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from feincms3 import plugins


class Article(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publication_date = models.DateTimeField(default=timezone.now)

    regions = [Region(key="main", title=_("Main"))]

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from feincms3.applications import reverse_app
        return reverse_app("blog", "article-detail", kwargs={"slug": self.slug})


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

class Html(plugins.html.HTML, PagePlugin):
    pass