# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Author, Tag, App, Release, NsRelease

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(App)
admin.site.register(Release)
admin.site.register(NsRelease)
