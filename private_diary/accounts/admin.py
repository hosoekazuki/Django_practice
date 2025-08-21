from django.contrib import admin
from .models import CustomUser
from diary.models import Diary


admin.site.register(CustomUser)
admin.site.register(Diary)