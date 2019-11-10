# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import *

admin.site.register(Instructor)
admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(SubSection)

# @admin.register(Course)
# class ViewAdmin(ImportExportModelAdmin):
#     pass