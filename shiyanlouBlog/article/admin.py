from django.contrib import admin
from article.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # fields = ['date_time','update_time']
    list_display = ('title','date_time', 'update_time',)
    ordering = ['-date_time']
admin.site.register(Article,ArticleAdmin)