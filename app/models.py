from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='todos')
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title