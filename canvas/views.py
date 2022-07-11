from django.shortcuts import render
from django.views import generic

from index.models import Content, Style
from .artist import *

import time
import sys
import tensorflow as tf

sys.path.append('C:/Users/micha/OneDrive/Documents/JupyterProjects/personal/imapainter/site')
from utils import utils

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'canvas/index.html'

  def get(self, request, content_id, style_id):
    content = Content.objects.get(id=content_id).content.path
    style = Style.objects.get(id=style_id).style.path
    content_img = preprocess_and_train(content, style)
    content_img = finalize(content_img)
    content_img = encode_img(content_img)
    context = {'content_img': content_img}
    return render(request, self.template_name, context=context)

def preprocess_and_train(content_img, style_img, epochs=300, optimizer=tf.keras.optimizers.Adam(learning_rate=0.01, beta_1=0.99, epsilon=1e-1)):
  content_img, style_img = resize_img(content_img, style_img)
  content_img, style_img = image_to_tensor(content_img, style_img)
  model, (content_target, style_target) = get_target(content_img, style_img)
  content_img = normalize_img(content_img)
  start = time.time()
  for epoch in range(epochs):
    utils.train_step(content_img, epoch, style_target, content_target, optimizer, model, start)
  end = time.time()
  print(f'Time taken for {epochs} epochs = {round(end - start, 2)} s')
  return content_img