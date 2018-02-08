from django.shortcuts import render, redirect
from django.views.generic.base import View

from home.models import Event


class HomeView(View):
    def get(self, request):

        qs = Event.objects.all().order_by('-timestamp')

        context = {
            'object_list': qs,
        }

        return render(request, 'home/home.html', context)


def delete(request, pk):

    Event.objects.get(pk=pk).delete()

    return redirect("/")