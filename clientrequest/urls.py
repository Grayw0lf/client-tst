from rest_framework import routers
from .views import RequisitionViewSet


app_name = 'client_request'

router = routers.SimpleRouter()
router.register('requisition', RequisitionViewSet)

urlpatterns = router.urls
