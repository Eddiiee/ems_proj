from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", EventListView.as_view()),
     path("events/", EventListView.as_view())
]