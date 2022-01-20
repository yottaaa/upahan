from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
# Create your models here.
class Profile(models.Model):
	fk_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	cp_no = models.CharField(max_length=20, blank=True, default="")
	address = models.CharField(max_length=200, blank=True, default="")
	date_created = models.DateTimeField(null=True,blank=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.fk_user.username

	def save(self, *args, **kwargs):
		self.date_created = timezone.now()
		super(Profile, self).save(*args,**kwargs)

class UserLogin(models.Model):
	fk_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(null=True,blank=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.fk_user.username

	def save(self, *args, **kwargs):
		self.date_created = timezone.now()
		super(UserLogin, self).save(*args,**kwargs)