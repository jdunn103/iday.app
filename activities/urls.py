from django.urls import path

from .views import ActivityCreateView

urlpatterns = [
    path('activities/', ActivityCreateView.as_view(), name='activity'),
]  