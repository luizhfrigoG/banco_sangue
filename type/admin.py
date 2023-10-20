from django.contrib import admin
from type.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('blood',)
