from django.contrib import admin

"""liste des modèles dont on peut modifier les instances "à la main" en tant qu'admin"""

from .models import Account,Serie,Season, Episode

admin.site.register(Account)
admin.site.register(Serie)
admin.site.register(Season)
admin.site.register(Episode)