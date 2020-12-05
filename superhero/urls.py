from django.urls import path
from superhero.views import AccordionView, HeroDetailView, HeroListView

urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('accordion/', AccordionView.as_view(), name='accordion'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
]