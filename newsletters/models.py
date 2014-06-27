from django.db import models


class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
