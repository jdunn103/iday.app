from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import ActivityForm, EventForm

from .models import Activity, Event

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy('my-account')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ActivityListView(ListView):
    model = Activity

class EventCreateView(CreateView):
    model = Event
    template_name = 'activities/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('event')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'activities/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('event')