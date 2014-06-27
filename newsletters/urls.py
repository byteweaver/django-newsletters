from django.conf.urls import url, patterns

from newsletters.views import SubscriptionDeleteView, SubscriptionFormView

urlpatterns = patterns('',
    url(r'^subscribe/$', SubscriptionFormView.as_view(), name='subscibe'),
    url(r'^unsubscribe/$', SubscriptionDeleteView.as_view(), name='unsubscribe'),
)
