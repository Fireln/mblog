from django.db import models
from django.utils import timezone
# Create your models here.

#分组
class Group(models.Model):

    group_name = models.CharField(max_length=200)
    creat_by_user = models.CharField(max_length=200,default='fireln')
    creat_time = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('creat_time',)
    def __str__(self):
        return self.group_name
    def get_id(self,name):
        return  Group.objects.filder(group_name=name).id

class Post(models.Model):

    group_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,default='fireln')
    body = models.TextField()
    creat_time = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=0)
    class Meta:
        ordering = ('creat_time',)

    def __str__(self):
        return self.title
    def get_post(self,name):
        group = Group()
        group_id = group.get_id(name=name)
        list = self.objects.all().filter(group_id=group_id)
        return list
