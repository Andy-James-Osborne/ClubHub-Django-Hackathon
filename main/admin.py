from django.contrib import admin
from .models import Events, Comment, User

# Register your models here.
admin.site.register(Events)
admin.site.register(Comment)
admin.site.register(User)