from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from .models import Event
from .forms import EventForm


class HomeView(CreateView):
    form_class = EventForm
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        qs = Event.objects.all()
        context['object_list'] = qs

        return context


def delete(request, pk=None):
    instance = get_object_or_404(Event, id=pk)
    instance.delete()
    return redirect("/")