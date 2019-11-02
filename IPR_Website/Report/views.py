from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Teams.models import Teams
from Skits.models import Skits
from Presentations.models import Presentations
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
# Create your views here.
class PresentationsDetailView(DetailView):
    model = Teams
    template_name = 'Report/template.html'
    def get_context_data(self,**kwargs):
        context = super(PresentationsDetailView, self).get_context_data(**kwargs)

        context['Presentation'] = Presentations.objects.filter(team_group_numbers=self.kwargs['pk'])
        context['skits'] = Skits.objects.filter(Q(team_group_number_1=self.kwargs['pk'])|Q(team_group_number_2=self.kwargs['pk']))
        return context

# id=self.kwargs['pk']