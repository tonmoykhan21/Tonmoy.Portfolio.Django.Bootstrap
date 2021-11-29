from django.contrib import admin
from django.db import models
from app_main.models import Home,About,Portfolio
# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=['name','designation','full_designation','updated',]
    search_fields=['name','designation','full_designation','updated',]
admin.site.register(Home,HomeAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=['heading','career','description','updated']
    search_fields=['heading','career','description','updated']

admin.site.register(About,AboutAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display=["link"]
    search_fields=['link']
admin.site.register(Portfolio,PortfolioAdmin)