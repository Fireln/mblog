from django.contrib import admin
from .models import Post,Group
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','creat_time')
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name','creat_by_user','creat_time')
admin.site.register(Post,PostAdmin)
admin.site.register(Group,GroupAdmin)