from django.db import models



class File(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)

class ChecklistItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    relatedFile = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)