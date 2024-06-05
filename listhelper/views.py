from django.shortcuts import render
from django.template.loader import render_to_string
from listhelper import models

# Create your views here.
def checklist(request, checklistId):
    checklist = models.Checklist.objects.get(id=checklistId)
    checklistItems = models.ChecklistHasChecklistItem.objects.filter(checklist=checklist)

    ctx = {
        'checklist_info' : checklist,
        'checklist_elements' : checklistItems,
        'editmode' : False,
    }
    string = render_to_string('listhelper/listview.html', ctx, request)
    return render(request, 'listhelper/listview.html', ctx)

def editChecklist(request, checklistId):
    checklist = models.Checklist.objects.get(id=checklistId)
    checklistItems = models.ChecklistHasChecklistItem.objects.filter(checklist=checklist)

    ctx = {
        'checklist_info' : checklist,
        'checklist_elements' : checklistItems,
        'editmode' : True,
    }
    string = render_to_string('listhelper/listview.html', ctx, request)
    return render(request, 'listhelper/listview.html', ctx)