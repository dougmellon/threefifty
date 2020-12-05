from django.views.generic import DetailView, ListView, TemplateView
from .models import Superhero

from os.path import exists


class AccordionView(TemplateView):
    template_name = "accordion.html"


class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero


class HeroDetailView(DetailView):
    template_name = "hero_card.html"
    model = Superhero

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/images' + image):
            kwargs['missing'] = True
        return kwargs

