from django.contrib import admin
from .models import Post, Report

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'desc','photo']
    
@admin.register(Report)
class ReportModelAdmin(admin.ModelAdmin):
    list_display=['name','email','username','message']
