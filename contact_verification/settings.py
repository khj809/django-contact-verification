from __future__ import unicode_literals
from django.conf import settings


CONTACT_VERIFICATION_SMS_TEXT = getattr(settings, 'CONTACT_VERIFICATION_SMS_TEXT', '{code}')
CONTACT_VERIFICATION_SENDER = getattr(settings, 'CONTACT_VERIFICATION_SENDER', '0000')
CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS = getattr(settings, 'CONTACT_VERIFICATION_ALLOW_MULTIPLE_CONTACTS', False)
