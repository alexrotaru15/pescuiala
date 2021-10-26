from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from .models import Balta, Recenzie


class RecenziiInLine(admin.TabularInline):
    model = Recenzie


class BaltiAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'details']}),
        ('Locatie', {
            'fields': ['location', 'county', 'map_page'],
        })
    ]
    inlines = [RecenziiInLine]
    list_display = ('name', 'location', 'date_added')
    search_fields = ['name', 'location']


class RecenzieAdmin(admin.ModelAdmin):
    list_display = ('balta', 'stars', 'title', 'date_added')
    list_filter = ['date_added', 'balta']


admin.site.register(Balta, BaltiAdmin)
admin.site.register(Recenzie, RecenzieAdmin)
