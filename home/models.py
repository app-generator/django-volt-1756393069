# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    crypto_balance = models.IntegerField(null=True, blank=True)
    wallet_number = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Crypto(models.Model):

    #__Crypto_FIELDS__
    bitcoin = models.IntegerField(null=True, blank=True)
    monero = models.IntegerField(null=True, blank=True)

    #__Crypto_FIELDS__END

    class Meta:
        verbose_name        = _("Crypto")
        verbose_name_plural = _("Crypto")



#__MODELS__END
