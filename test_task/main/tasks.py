from test_task.celery import app
from .models import Function
from datetime import datetime


@app.task
def create_date_of_processing(pk):
    func = Function.objects.get(pk=pk)
    func.date_of_processing = datetime.utcnow()
    func.save()
