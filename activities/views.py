from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import ActivityForm

from .models import Activity

class ActivityView(CreateView):
    model = Activity
    form_class = ActivityForm
    # template_name = "activities/activity_form.html"
    success_url = reverse_lazy('my-account')
