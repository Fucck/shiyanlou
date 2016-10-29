from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    label = models.CharField(max_length=50,blank=True)
    date_time = models.DateTimeField('创建日期',auto_now_add=True)
    update_time = models.DateTimeField('更新日期',auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-date_time"]