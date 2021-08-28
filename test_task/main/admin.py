from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

from .models import *
from .tasks import create_date_of_processing
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
import time


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    fields = ['formula', 'interval', 'step']
    list_display = ['formula', 'get_graph', 'interval', 'step', 'date_of_processing']
    list_filter = ['date_of_processing']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Вызов celery task
        create_date_of_processing.apply_async((obj.pk,), eta=timezone.now() + timedelta(seconds=5))

    def get_graph(self, object):
        if object.picture:
            return mark_safe(f"<img src='{object.picture.url}' width=200>")
