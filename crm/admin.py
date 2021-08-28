from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm
# Register your models here.

class Comment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_text', 'coment_date')
    readonly_fields = ('coment_date',)
    extra = 0




class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_name', 'order_status', 'order_phone', 'order_date')
    list_display_links = ('id','order_name',)
    search_fields = ('order_name','id')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_name', 'order_phone', 'order_status', 'order_date')
    readonly_fields = ('order_date','id')
    inlines = [Comment,]



admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)

