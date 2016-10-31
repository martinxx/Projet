from django.contrib import admin

# Register your models here.

from .models import Account,Serie,Season

admin.site.register(Account)
admin.site.register(Serie)
admin.site.register(Season)