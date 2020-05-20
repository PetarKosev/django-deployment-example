from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    #additional classes
    portfolio_site = models.URLField(blank='true')

    profile_pic = models.ImageField(upload_to='profile_pics',blank='true')

    def __str__(self):
        return self.user.username
