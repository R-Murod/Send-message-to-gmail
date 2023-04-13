from django.db import models


# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    sent_at = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} --> {self.email} -- > {self.sent_at}'