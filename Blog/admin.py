from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Posts, Comment

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Comment)
