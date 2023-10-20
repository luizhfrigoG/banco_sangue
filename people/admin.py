from django.contrib import admin
from people.models import People

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('nome', 'type_blood', 'cpf', 'email', 'sex')
