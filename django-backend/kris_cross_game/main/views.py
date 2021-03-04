from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def main(req):
    return render(req, 'html/main.html')
