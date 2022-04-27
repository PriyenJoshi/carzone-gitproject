from django.shortcuts import render

# Create your views here.
def home(request):
     #whenever below path is hit it will redirect to templates folder in which pages folder inside that home.html file
    return render(request, 'pages/home.html')