from django.contrib import admin

from .models import Fine, Team, UserFineHistoric

admin.site.register(Fine)
admin.site.register(Team)
admin.site.register(UserFineHistoric)
