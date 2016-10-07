from django.db import models

# Create your models here.


class Set(models.Model):
    pass


class Conversation(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    user = models.CharField(max_length=2500)
    emily = models.CharField(max_length=2500)
