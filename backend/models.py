from django.db import models

class Track(models.Model):
  title = models.CharField(max_length=111)
  description = models.TextField(max_length=9000)

  def __str__(self):
    return self.title
