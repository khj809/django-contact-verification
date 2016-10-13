from django.db import models
import datetime


class ContactVerificationQuerySet(models.QuerySet):
    def awaiting(self):
        expiry_datetime = datetime.datetime.now()-datetime.timedelta(minutes=3)
        return self.filter(created__gte=expiry_datetime)

    def inactive(self):
        expiry_datetime = datetime.datetime.now()-datetime.timedelta(minutes=3)
        return self.filter(created__lt=expiry_datetime)
