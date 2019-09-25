from django.shortcuts import render
from .models import Teams
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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



class TeamsCreateView(CreateView):
    model = Teams
    fields = ['team_number', 'member_1', 'member_2', 'member_3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TeamsDetailView(DetailView):
    model = Teams

class TeamsUpdateView(UpdateView):
    model = Teams
    fields = ['team_number', 'member_1', 'member_2', 'member_3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TeamsDeleteView(DeleteView):
    model = Teams
    success_url = '/teams/'
