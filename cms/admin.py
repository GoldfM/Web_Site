from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Carusel
# Register your models here.

class CmsAdm(admin.ModelAdmin):
    list_display = ('carusel_title', 'carusel_text', 'carusel_css', 'ShowImage')
    list_display_links = ('carusel_title',)
    list_editable = ('carusel_css',)

    def ShowImage(self, obj):
        return mark_safe(f'<img src="{obj.carusel_img.url}", width="80px">')


admin.site.register(Carusel, CmsAdm)