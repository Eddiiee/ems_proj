from django.shortcuts import render

from events.models import Event
from .models import Registration
# Create your views here.
 from django.views.generic import TemplateView

 class RegistrationsListView(TemplateView):
    template_name = "registration_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["even"] = Event.objects.filter(pk = self.kwargs['event_pk']).first()

        data["participants"] = Registration.objects.filter(event=self.kwargs['event_pk'])
    return data

 class JoinEventView(CreateView):
     model = Registration
     fields = ['parents_permit', 'parents_contact_number', 'waiver']
     template_name = "event_join.html"
  
    def form_valid(self, form):
        form.instance.event = Event.objects.filter(pk=self.kwargs["event_pk"]).first()
        form.instance.participants = self.request.user
        return super().form_valid(form)
