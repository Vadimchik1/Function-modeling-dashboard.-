from test_task.celery import app
from .models import Function
from datetime import datetime
from .service import generate_image, generate_ex_image
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


@app.task
def generate_graph(pk):
    func_obj = Function.objects.get(pk=pk)
    func_string = func_obj.formula
    try:
        picture = generate_image(func_string, func_obj.interval, func_obj.step)

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(picture)
        img_temp.flush()

        func_obj.picture.save(f'image/{pk}.png', File(img_temp), save=True)

    except Exception as ex:
        ex_image = generate_ex_image(str(ex))
        img_temp_ex = NamedTemporaryFile(delete=True)
        img_temp_ex.write(ex_image)
        img_temp_ex.flush()
        func_obj.picture.save(f'image/{pk}.png', File(img_temp_ex), save=True)
    finally:
        func_obj.date_of_processing = datetime.utcnow()
        func_obj.save()
