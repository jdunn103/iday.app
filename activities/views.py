from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import ActivityForm

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
    fields = ['activity']

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'activities/event_update.html'
    fields = []
    success_url = reverse_lazy('activity-list')

    def form_valid(self, form):
        form.instance.end_time = timezone.now()
        return super().form_valid(form)