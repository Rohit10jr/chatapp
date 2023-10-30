from django.shortcuts import render

# rohit@mail.com rohit 1234

def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')