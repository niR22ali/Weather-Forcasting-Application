from django.contrib import admin
from .models import thing

# Register your models here.

class thingshow(admin.ModelAdmin):
    list_display = ('thingName','thingPrice')

admin.site.register(thing,thingshow)



