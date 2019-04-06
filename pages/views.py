from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'pages/contact.html', {'title': 'Contact'})

