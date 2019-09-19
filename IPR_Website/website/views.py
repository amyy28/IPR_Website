from django.shortcuts import render, redirect

def home(request):
    context = {
        "about": "active",
    }
    return render(request, 'website/about.html', context)

