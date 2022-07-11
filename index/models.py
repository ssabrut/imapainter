from django.db import models

# Create your models here.
class Content(models.Model):
  image = models.FileField(upload_to='images/', name='content', max_length=255, null=True)

  class Meta:
    db_table = 'contents'
    verbose_name = 'Content'
    verbose_name_plural = 'Contents'
  
class Style(models.Model):
  image = models.FileField(upload_to='images/', name='style', max_length=255, null=True)

  class Meta:
    db_table = 'styles'
    verbose_name = 'Style'
    verbose_name_plural = 'Styles'