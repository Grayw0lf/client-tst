from django.contrib import admin
from .models import Responsible, Requisition, Client


@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):
    fields = ['fio', 'position']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['fio', 'phone']


@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    fields = ['date', 'tetx', 'responsible', 'client']
