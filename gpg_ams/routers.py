from rest_framework import routers
from client.views import ClientViewSet
from jobrequest.views import JobRequestViewSet


router = routers.DefaultRouter()

router.register(r'client', ClientViewSet)
router.register(r'jobrequest', JobRequestViewSet)
