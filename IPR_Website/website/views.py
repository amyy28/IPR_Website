from django.shortcuts import render, redirect
from .models import team
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

def home(request):
    context = {
        "about": "active",
    }
    return render(request, 'website/about.html', context)

class createteam(CreateView):
    model = team
    fields = ['team_group_number', 'team_member_1','team_member_2','team_member_3','team_usn_1','team_usn_2','team_usn_3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class saveteam(DetailView):
    model = team


