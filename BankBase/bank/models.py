from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# user field er username,password,email, firstname,lastname


# for adding sth that isnt present in user model
class UserInfo(models.Model):
    # userinfo -one to one- user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    facebook_id = models.URLField(blank=True)
    # profile_pics -directory- te save hobe
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
