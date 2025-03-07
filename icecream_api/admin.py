from django.contrib import admin

from icecream_api.models.command_related import Command
from icecream_api.models.item_related import Batch, Item

# Register your models here.

admin.site.register(Item)
admin.site.register(Batch)
admin.site.register(Command)
