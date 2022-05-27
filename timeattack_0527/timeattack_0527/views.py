from django.shortcuts import render


def index_response(request):
    return render(request, 'index.html')

