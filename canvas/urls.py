from django.urls import path
from . import views

app_name = 'canvas'
urlpatterns = [
  path('<int:content_id>/<int:style_id>/', views.IndexView.as_view(), name='index'),
]