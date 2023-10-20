from django.contrib import admin
from sex.models import Sex


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('name',)