from django.urls import path

from .views import ActivityCreateView, ActivityListView

urlpatterns = [
    path('activities-create/', ActivityCreateView.as_view(), name='activity-create'),
    path('activities-list/', ActivityListView.as_view(), name='activity-list'),
]  