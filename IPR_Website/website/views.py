from django.shortcuts import render

def home(request):
    context = {
        "about": "active",
    }
    return render(request, 'website/about.html', context)


def AboutUs(request):
    context = {
        "AboutUs": "active",
    }
    return render(request, 'website/AboutUs.html', context)