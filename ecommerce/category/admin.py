from django.contrib import admin

from .models import Category

# Register your models here.

class CategoryAdmin( admin.ModelAdmin ):
    #indicamos que el campo slug se llene automaticamente con el valor del campo category_name
    #ejemplo: si escribes "ropa de verano" el slug seria "ropa-de-verano"
    prepopulated_fields = { 'slug': ( 'category_name', ) }
    list_display = ( 'category_name', 'slug' )


admin.site.register( Category, CategoryAdmin )
