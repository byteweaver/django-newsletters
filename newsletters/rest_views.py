from rest_framework import viewsets

from newsletters.models import Subscription
from newsletters.permissions import IsAuthenticatedOrCreateOnly
from newsletters.serializers import SubscriptionSerializer
from newsletters.utils import get_client_ip


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def create(self, request, *args, **kwargs):
        request.data['ip'] = get_client_ip(request)
        return super(SubscriptionViewSet, self).create(request, args, kwargs)
