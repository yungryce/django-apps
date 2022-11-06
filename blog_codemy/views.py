from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Reg

# Create your views here.
# def index(request):
#     return render(request, 'blog_codemy/index.html')

class Homeview(ListView):
    model = Reg
    template_name = 'blog_codemy/home.html'


class DetailV(DetailView):
    model = Reg
    template_name = 'blog_codemy/art_det.html'

class Formview(CreateView):
    model = Reg
    template_name = 'blog_codemy/forms.html'
    fields = '__all__'
    # fields = ('title', 'body')