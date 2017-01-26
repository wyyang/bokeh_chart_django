import sys
import os
from django.conf import settings
from bokeh.charts import Scatter
from bokeh.sampledata.autompg import autompg as df
from bokeh.embed import components
from django.shortcuts import render

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'uzt7bkn9m)3h6(^)h8n7&q%&ux#ftgzx@jqk67y3z1aa-__*qv')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    MIDDLEWARE_CLASSES={
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    },
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (os.path.join(BASE_DIR, 'templates'), ),
        },
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application


def index(request):
    p = Scatter(df, x='displ', y='hp', color='cyl',
                title="HP vs DISPL (shaded by CYL)", legend="top_left",
                legend_sort_field = 'color',
                legend_sort_direction = 'ascending',
                xlabel="Displacement",
                ylabel="Horsepower")
    script, div = components(p)
    return render(request, 'index.html', {'div': div, 'script': script})


urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    from django.conf import settings

    execute_from_command_line(sys.argv)
