from django.views.generic import CreateView, DeleteView

from rest_framework import viewsets

from newsletters.models import Subscription
from newsletters.forms import SubscriptionForm
from newsletters.serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionCreateView(CreateView):
    form_class = SubscriptionForm


class SubscriptionDeleteView(DeleteView):
    model = Subscription
