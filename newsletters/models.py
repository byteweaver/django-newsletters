from django.utils.translation import ugettext as _
from django.db import models


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')

    def __str__(self):
        return self.email
