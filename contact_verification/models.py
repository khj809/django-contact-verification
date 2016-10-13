# coding=utf-8
from __future__ import unicode_literals
from random import randint

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from contact_verification.data import COUNTRY_PHONES
from contact_verification.validators import PhoneNumberValidator
from .managers import ContactVerificationQuerySet


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contacts")
    country_number = models.CharField(max_length=10, choices=COUNTRY_PHONES)
    phone_number = models.CharField(max_length=100, validators=[PhoneNumberValidator()])

    class Meta:
        verbose_name = _("연락처")
        verbose_name_plural = _("연락처")
        unique_together = ['country_number', 'phone_number']

    def __unicode__(self):
        return "{}-{}".format(self.country_number, self.phone_number)

    def save(self, *args, **kwargs):
        if self.phone_number and self.phone_number[0] == '0':
            self.phone_number = self.phone_number[1:]
        super(Contact, self).save(*args, **kwargs)


class ContactVerification(models.Model):
    country_number = models.CharField(max_length=10, choices=COUNTRY_PHONES)
    phone_number = models.CharField(max_length=100, validators=[PhoneNumberValidator()])
    code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    objects = ContactVerificationQuerySet.as_manager()

    class Meta:
        verbose_name = _("연락처 인증")
        verbose_name_plural = _("연락처 인증")
        # unique_together = ['country_number', 'phone_number']

    def __unicode__(self):
        return "%s %s" % (self.contact, self.code)

    @staticmethod
    def generate_code():
        return str(randint(10000, 99999))

    def is_awaiting(self):
        return ContactVerification.objects.awaiting().filter(id=self.id).exists()

    def save(self, *args, **kwargs):
        pin_exists = ContactVerification.objects.awaiting().filter(
            country_number=self.country_number, phone_number=self.phone_number
        ).exists()
        if not pin_exists:
            if not self.code:
                self.code = ContactVerification.generate_code()
            if self.phone_number and self.phone_number[0] == '0':
                self.phone_number = self.phone_number[1:]
            super(ContactVerification, self).save(*args, **kwargs)
