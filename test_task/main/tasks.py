from test_task.celery import app
from .models import Function
from datetime import datetime
from .service import generate_image
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponseRedirect

@app.task
def create_date_of_processing(pk):
    func_obj = Function.objects.get(pk=pk)
    func_string = func_obj.formula
    picture = generate_image(func_string, func_obj.interval, func_obj.step, pk)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(picture)
    img_temp.flush()

    func_obj.picture.save(f'image/{pk}.png', File(img_temp), save=True)
    func_obj.date_of_processing = datetime.utcnow()
    func_obj.save()
    HttpResponseRedirect('admin/main/function/')




