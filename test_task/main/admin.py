from django.contrib import admin
from .models import *
from .tasks import create_date_of_processing


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    fields = ['formula', 'interval', 'step']
    list_display = ['formula', 'picture', 'interval', 'step', 'date_of_processing']
    list_filter = ['date_of_processing']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Вызов celery task
        create_date_of_processing.delay(pk=obj.pk)

