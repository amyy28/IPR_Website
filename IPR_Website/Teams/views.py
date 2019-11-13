from django.shortcuts import render
from .models import Teams
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Report.views import PresentationsDetailView

@login_required
def teams(request):
    teams = Teams.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        teams = teams.filter(
            Q(team_number__icontains=search_term)
        )
    context = {
        "teams": "active", 'teams': teams, 'search_term': search_term
    }
    return render(request, 'Teams/teams.html', context)



class TeamsCreateView(LoginRequiredMixin, CreateView):
    model = Teams
    fields = ['team_number', 'member_1','member_1_USN', 'member_2','member_2_USN','member_3','member_3_USN','group_photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TeamsDetailView(LoginRequiredMixin, DetailView):
    model = Teams

class TeamsUpdateView(LoginRequiredMixin, UpdateView):
    model = Teams
    fields = ['team_number', 'member_1','member_1_USN', 'member_2','member_2_USN','member_3','member_3_USN','group_photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TeamsDeleteView(LoginRequiredMixin, DeleteView):
    model = Teams
    success_url = '/teams/'
