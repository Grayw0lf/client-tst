from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Requisition
from .serializers import RequisitionSerialize


class RequisitionViewSet(ModelViewSet):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerialize
    permission_classes = [IsAuthenticatedOrReadOnly]
