from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import ActivityForm

from .models import Activity

class ActivityCreateView(CreateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy('my-account')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ActivityListView(ListView):
    model = Activity