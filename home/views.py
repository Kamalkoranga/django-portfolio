from django.shortcuts import render

def home_index(request):
    name = 'Home'
    return render(request, 'home_index.html', {'name': name})