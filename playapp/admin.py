from django.contrib import admin
from .models import Orangecap , Purplecap


class OrangecapAdmin(admin.ModelAdmin):
    list_display = ('name','img_url')


admin.site.register(Orangecap,OrangecapAdmin)


class PurplecapAdmin(admin.ModelAdmin):
    list_display = ('name','img_url')


admin.site.register(Purplecap,PurplecapAdmin)




# Register your models here.
