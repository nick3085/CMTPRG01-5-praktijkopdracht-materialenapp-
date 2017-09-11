from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.template.loader import render_to_string

from .models import Delivery, Category, Location, Supplier


# Deliveries admin class for searching deliveries and filtering
# see delivery model for more information
class DeliveryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        'date', 'location', 'supplier', 'weight', 'processing', 'categories_to_string', 'notes', 'image',
    )
    list_display_links = ('date',)
    ordering = ('-date',)
    list_per_page = 50

# Register your models here.
admin.site.site_header = 'Buurman - Materialmanager'
admin.site.register(Location)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Delivery, DeliveryAdmin)