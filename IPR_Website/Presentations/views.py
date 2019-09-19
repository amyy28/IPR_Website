from django.shortcuts import render, redirect

def presentations(request):
    context = {
        "presentations": "active",
    }
    return render(request, 'Presentations/presentations.html', context)
