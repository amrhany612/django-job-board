from ast import Import


import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
   
    title = django_filters.CharFilter(lookup_expr='icontains') 
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = job
        fields = '__all__'
        exclude = ['owner','Image','slug','published_at','salary','Vacancy']