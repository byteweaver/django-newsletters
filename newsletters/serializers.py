from rest_framework import serializers

from newsletters.models import Subscription


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ('email', 'ip', 'created_at')
