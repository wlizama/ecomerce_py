from django.db import models
from django.conf import settings

class Comment(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  content = models.TextField()
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='comments'
  )

  def __str__(selft):
    return selft.conten[:20]
