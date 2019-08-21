from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)#创建的时候就保存当前时间
    def __str__(self):
        return self.title
