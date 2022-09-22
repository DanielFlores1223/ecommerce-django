from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin( UserAdmin ):
    #campos que se mostraran en la tabla de todos los registros
    list_display = ( 'email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active', )
    #campos para indicar que campos se mostraran como link en la tabla para mostrar mas info
    list_display_links = ( 'email', 'first_name', 'last_name', )
    #campos de solo lectura
    readonly_fields = ( 'last_login', 'date_joined', ) #automaticamente pone el campo password en readonly
    #en que orden se mostraran los registros
    ordering = ('-date_joined',)
    filter_horizontal = ()
    #listar filtros en el admin
    list_filter = ( 'email', )
    fieldsets = ()

# Register your models here.
admin.site.register( Account, AccountAdmin )