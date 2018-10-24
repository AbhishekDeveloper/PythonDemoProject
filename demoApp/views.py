from django.shortcuts import render

# Create your views here.


def home(request):
    packages = [
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
