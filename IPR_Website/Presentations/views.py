from django.shortcuts import render
from .models import Presentations
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def presentations(request):
    presentations = Presentations.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        presentations = presentations.filter(
            Q(team_group_numbers__icontains=search_term) |
            Q(topic__icontains=search_term)
        )
    context = {
        "presentations": "active", 'presentations': presentations, 'search_term': search_term
    }
    return render(request, 'Presentations/presentations.html', context)


class PresentationsCreateView(LoginRequiredMixin, CreateView):
    model = Presentations
    fields = ['team_group_numbers', 'topic', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PresentationsDetailView(LoginRequiredMixin, DetailView):
    model = Presentations

class PresentationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Presentations
    fields = ['team_group_numbers', 'topic', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PresentationsDeleteView(LoginRequiredMixin, DeleteView):
    model = Presentations
    success_url = '/presentations/'
