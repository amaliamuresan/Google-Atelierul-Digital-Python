from django.urls import reverse
from django.views.generic import CreateView, ListView

from aplicatie1.models import Location


class CreateIndexView(CreateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:adaugare')

class HomeIndex(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'