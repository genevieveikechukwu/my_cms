from django.contrib import admin

from .models import user, template, setting, page, page_field
# Register your models here.
admin.site.register (user)
admin.site.register (template)
admin.site.register (setting)
admin.site.register (page)
admin.site.register (page_field)
