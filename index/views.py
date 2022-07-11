import math
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from canvas.models import Result
from django.db.models import Avg
from .forms import *

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'index/index.html'

  def get(self, request):
    time_taken = math.ceil(Result.objects.aggregate(Avg('time_taken'))['time_taken__avg'])
    context = {
      'content_form': ContentForm(),
      'style_form': StyleForm(),
      'time_taken': time_taken
    }
    return render(request, self.template_name, context=context)
  
  def post(self, request):
    content_form = ContentForm(request.POST, request.FILES)
    style_form = StyleForm(request.POST, request.FILES)
    if content_form.is_valid() and style_form.is_valid():
      content = content_form.save()
      style = style_form.save()
      return self.get_success_url(content_id=content.id, style_id=style.id)
    context = {
      'content_form': ContentForm(),
      'style_form': StyleForm()
    }
    return render(request, self.template_name, context=context)

  def get_success_url(self, **kwargs):
    return HttpResponseRedirect(reverse_lazy('canvas:index', kwargs=kwargs))