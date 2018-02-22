from django.db import models
'''Extend USER fileds'''
from django.conf import settings
from django.contrib.auth.models import User


'''
Extend built-in django user model with extra information/fields
PROFILE wiht 1 to 1 relationship
'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def __repr__(self):
        return self._repr()