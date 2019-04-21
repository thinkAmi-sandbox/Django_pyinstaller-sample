from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
import platform
from myapp.models import Fruit


def hello(request):
    return HttpResponse('Hello, world')


class FruitTemplateView(TemplateView):
    template_name = 'myapp/fruit.html'
    extra_context = {
        'base_dir': settings.BASE_DIR,
        'python_version': platform.python_version(),
        'fruits': Fruit.objects.all(),
    }
