from django.contrib import admin

from .models import Activity, Event

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    list_display = ['name', 'created', 'updated', 'user']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')

        return ()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['activity', 'created', 'updated', 'start_time', 'end_time', 'duration', 'slug']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')

        return ()

