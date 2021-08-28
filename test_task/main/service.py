import re
import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt
import numpy as np
from test_task.settings import MEDIA_ROOT
import base64
from io import BytesIO

replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    't',
    'sin',
    'cos',
    'sqrt',
    'exp',
]


def string_to_func(string):
    ''' evaluates the string and returns a function of t '''
    # find all words and check if all are allowed:
    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(t):
        return eval(string)

    return func


def generate_image(func_string, interval, step, pk):
    buffer = BytesIO()
    f = string_to_func(func_string)
    t = np.linspace(-interval, interval, step)
    fig = plt.figure()
    plt.plot(t, f(t))
    plt.xlim(-interval, interval)
    # picture_path = f'{MEDIA_ROOT}/pictures/{str(pk)}.png'
    fig.savefig(buffer, dpi=500, format='png')
    buffer.seek(0)
    picture_png = buffer.getvalue()
    image = base64.b64encode(picture_png)
    image = image.decode('UTF-8')
    buffer.close()
    return picture_png
