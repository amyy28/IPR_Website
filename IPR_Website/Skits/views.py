from django.shortcuts import render, redirect

def skits(request):
    context = {
        "skits": "active",
    }
    return render(request, 'Skits/skits.html', context)