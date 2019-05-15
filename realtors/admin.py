from django.contrib import admin

from . models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'is_mvp', 'email', 'hire_date')
    list_display_links = ('id', 'nombre')
    list_editable = ('is_mvp',)
    search_fields = ('nombre',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
