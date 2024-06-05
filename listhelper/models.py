from django.db import models



class File(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.name} -> {self.path}"

class ChecklistItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    relatedFile = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} -> {self.relatedFile}"

class Checklist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.name}"

class ChecklistHasChecklistItem(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    item = models.ForeignKey(ChecklistItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.checklist} -> {self.item}"