from django.contrib import admin
from listhelper import models

# Register your models here.
admin.site.register(models.ChecklistItem)
admin.site.register(models.File)
admin.site.register(models.Checklist)
admin.site.register(models.ChecklistHasChecklistItem)