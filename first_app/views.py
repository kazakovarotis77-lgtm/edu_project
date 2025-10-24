from django.shortcuts import render
from .models import Lesson
from django.views.generic import DetailView
from .models import Salom

def home(request):
    darslar = Lesson.objects.all()
    return render(request, 'index.html', {"HTML_Dars": darslar})

class Salom_Detail(DetailView):
    model = Salom
    template_name = 'salom_detail.html'
    context_object_name = 'detail'
