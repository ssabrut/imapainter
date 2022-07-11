from django.db import models

# Create your models here.
class Result(models.Model):
  time_taken = models.FloatField(null=True)

  class Meta:
    db_table = 'results'
    verbose_name = 'Result'
    verbose_name_plural = 'Results'