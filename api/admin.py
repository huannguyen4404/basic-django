from django.contrib import admin
from .models import Bucket
# Register your models here.
class BucketAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Bucket, BucketAdmin)
