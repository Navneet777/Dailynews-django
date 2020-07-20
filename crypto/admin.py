from django.contrib import admin
# Register your models here.
from crypto.models import Contactmodel , Subscribe

class ContactmodelAdmin(admin.ModelAdmin):
    list_display = ['name','email','messages']

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']
admin.site.register(Contactmodel,ContactmodelAdmin)
