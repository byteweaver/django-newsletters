from django.forms import ModelForm

from newsletters.models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
