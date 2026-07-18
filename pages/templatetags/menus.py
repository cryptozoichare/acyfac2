from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def main_menu():
    return Page.objects.with_tree_fields().active().filter(parent=None)