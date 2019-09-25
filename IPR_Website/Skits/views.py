from django.shortcuts import render
from .models import Skits
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def skits(request):
    skits = Skits.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        skits = skits.filter(
            Q(team_group_numbers__icontains=search_term) |
            Q(topic__icontains=search_term)
        )
    context = {
        "skits": "active", 'skits': skits, 'search_term': search_term
    }
    return render(request, 'Skits/skits.html', context)



class SkitsCreateView(CreateView):
    model = Skits
    fields = ['team_group_numbers', 'topic', 'video_url', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SkitsDetailView(DetailView):
    model = Skits

class SkitsUpdateView(UpdateView):
    model = Skits
    fields = ['team_group_numbers', 'topic', 'video_url', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SkitsDeleteView(DeleteView):
    model = Skits
    success_url = '/skits/'