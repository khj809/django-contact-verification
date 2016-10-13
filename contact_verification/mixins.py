# coding=utf-8
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _

from .models import Pin


class ContactVerificationFormMixin(object):
    code = forms.CharField(label='인증코드')
    contact_field_name = 'contact'

    class Media:
        js = ('/static/contact_verification/contact_verification.js',)

    def __init__(self, *args, **kwargs):
        super(ContactVerificationFormMixin, self).__init__(*args, **kwargs)

        if hasattr(self.Meta, 'contact_field_name'):
            self.contact_field_name = self.Meta.contact_field_name

    def save(self, commit=True):
        instance = super(ContactVerificationFormMixin, self).save(commit)
        contact = self.cleaned_data[self.contact_field_name]
        code = self.cleaned_data['code']

        if code:
            pin = Pin.objects.get(contact=contact, code=code)
            pin.is_verified = True
            pin.save()
        return instance

    def clean(self):
        cleaned_data = super(ContactVerificationFormMixin, self).clean()
        contact = cleaned_data.get(self.contact_field_name)
        code = cleaned_data.get("code")

        # hook for extra contact verification validation
        self.clean_contact_verification(contact, code)

        if code and not Pin.objects.awaiting().filter(contact=contact, code=code).exists():
            if Pin.objects.filter(contact=contact, code=code).exists():
                msg = _('인증코드가 만료되었습니다.')
            else:
                msg = _('번호를 인증할 수 없습니다.')
            self.add_error('code', msg)

    def clean_contact_verification(self, contact, code):
        pass