from django.shortcuts import render_to_response

from test_app.models import TestModel

from django.forms.models import ModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView


class TestForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = TestModel


class ModelListView(ListView):
    model = TestModel
    template_name = "list.html"


class ModelCreateView(CreateView):
    model = TestModel
    template_name = "form.html"


class ModelDetailView(DetailView):
    model = TestModel
    template_name = "detail.html"

    # def dispatch(self, request, *args, **kwargs):
    #     print(request, *args, **kwargs)

class ModelEditView(UpdateView):
    model = TestModel
    template_name = "form.html"
