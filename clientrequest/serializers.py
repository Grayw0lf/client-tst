from rest_framework.serializers import ModelSerializer
from .models import Client, Responsible, Requisition


class ResponsibleSerializer(ModelSerializer):
    class Meta:
        model = Responsible
        fields = ['id', 'fio', 'position']


class ClientSerialize(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'fio', 'phone']


class RequisitionSerialize(ModelSerializer):
    responsible = ResponsibleSerializer()
    client = ClientSerialize()

    class Meta:
        model = Requisition
        fields = ['id', 'text', 'date', 'responsible', 'client']
