from django.views.generic import CreateView, DeleteView

from newsletters.models import Subscription
from newsletters.forms import SubscriptionForm


class SubscriptionCreateView(CreateView):
    form_class = SubscriptionForm


class SubscriptionDeleteView(DeleteView):
    model = Subscription
