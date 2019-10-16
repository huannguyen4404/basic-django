from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
    # response = HttpResponse()
    # response.writelines("<h1>Hi</h1>")
    # response.write('Print from home app')
    # return response
def contact(request):
    return render(request, 'pages/contact.html')
    
def error404(request, exception):
    return render(request, 'pages/error.html')
def error500(request):
    return render(request, 'pages/error.html')
