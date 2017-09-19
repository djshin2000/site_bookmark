#-*-coding: utf-8-*-

from django.contrib import admin
from .models import Bookmark
# from bookmark.models import Bookmark 위와 같은 내용

# Register your models here.

admin.site.register(Bookmark)
