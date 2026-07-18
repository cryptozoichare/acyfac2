from django.db import models

from content_editor.models import Region, create_plugin_base
from django.utils.translation import gettext_lazy as _
from django_prose_editor.fields import ProseEditorField

from feincms3.applications import ApplicationType, PageTypeMixin, TemplateType
from feincms3.mixins import LanguageMixin, MenuMixin
from feincms3 import plugins
from feincms3.pages import AbstractPage



class Page(AbstractPage, PageTypeMixin, MenuMixin, LanguageMixin):
    TYPES = [
        TemplateType(
            key="standard",
            title=_("standard"),
            template_name="pages/standard.html",
            regions=[Region(key="main", title=_("Main"))],
        ),
        ApplicationType(
            key="blog",
            title=_("blog"),
            urlconf="blog.urls",
        ),
    ]

    MENUS = [("main", _("main"))]


PagePlugin = create_plugin_base(Page)


class RichText(plugins.richtext.RichText, PagePlugin):
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


class Image(plugins.image.Image, PagePlugin):
    pass

class Html(plugins.html.HTML, PagePlugin):
    pass