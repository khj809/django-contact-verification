# coding=utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from contact_verification.data import COUNTRY_PHONES
from contact_verification.models import Contact, ContactVerification
from contact_verification.serializers import ContactVerificationSerializer, ContactSerializer, CountrySerializer


class ContactVerificationViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = ContactVerification.objects.all()
    serializer_class = ContactVerificationSerializer
    permission_classes = (AllowAny,)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ContactVerificationViewSet, self).dispatch(request, *args, **kwargs)


class ContactViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ContactViewSet, self).dispatch(request, *args, **kwargs)


class CountryViewSet(ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return [{'number': country[0], 'name': country[1]} for country in COUNTRY_PHONES]
