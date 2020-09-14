from django.urls import path

from .views import ActivityCreateView, ActivityListView, EventCreateView, EventUpdateView

urlpatterns = [
    path('events/<slug>/', EventUpdateView.as_view(), name='event-update'),
    path('activities-create/', ActivityCreateView.as_view(), name='activity-create'),
    path('activities-list/', ActivityListView.as_view(), name='activity-list'),
    path('events/', EventCreateView.as_view(), name='event-create'),
]  