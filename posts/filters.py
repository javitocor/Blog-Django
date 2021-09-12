import django_filters
from .models import *
from django import forms

class PostFilter(django_filters.FilterSet):
    headline = django_filters.CharFilter(lookup_expr='icontains', label="")
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
    class Meta:
        model = Post
        fields = ['headline', 'tags']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(PostFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['headline'].field.widget.attrs.update({'class': 'form-control', 'placeholder':'Search in Headlines'})