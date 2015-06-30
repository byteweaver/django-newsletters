from django.views.generic import CreateView, DeleteView

from rest_framework import viewsets

from newsletters.models import Subscription
from newsletters.forms import SubscriptionForm
from newsletters.serializers import SubscriptionSerializer
from newsletters.utils import get_client_ip


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        request.data['ip'] = get_client_ip(request)
        return super(SubscriptionViewSet, self).create(request, args, kwargs)


class SubscriptionCreateView(CreateView):
    form_class = SubscriptionForm


class SubscriptionDeleteView(DeleteView):
    model = Subscription
