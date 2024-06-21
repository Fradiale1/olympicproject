from django.contrib import admin
from .models import Host, Athlete, Medal, Result

admin.site.register(Host)
admin.site.register(Athlete)
admin.site.register(Medal)
admin.site.register(Result)