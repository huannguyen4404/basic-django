from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

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
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'pages/register.html', {'form': form})
