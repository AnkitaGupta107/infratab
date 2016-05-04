from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    SMS = 'SMS'
    EMAIL = 'EMAIL'

    REMINDER_TYPES = ((SMS, 'sms'),
                      (EMAIL, 'email'))

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    remark = models.CharField(max_length=255)
    reminder_type = models.CharField(choices=REMINDER_TYPES, max_length=10)

    def __unicode__(self):
        return self.remark

