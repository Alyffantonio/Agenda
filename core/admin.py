from django.contrib import admin
from core.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','title', 'date_event','date_creation')
    list_filter = ('user','title','date_event')


admin.site.register(Event,EventAdmin)
