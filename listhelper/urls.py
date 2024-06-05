from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('checklist/view/<checklistId>', views.checklist, name = 'list.checklist'),
    path('checklist/edit/<checklistId>', views.editChecklist, name = 'list.checklist'),
    #path('checklist/new/', views.newChecklist, name = 'list.checklist'), #TODO
    
    #path('item/view/<itemId>', views.newChecklistItem, name = 'list.checklist'), #TODO
    #path('item/edit/<itemId>', views.newChecklistItem, name = 'list.checklist'), #TODO
    #path('item/new/', views.newChecklistItem, name = 'list.checklist'), #TODO
]