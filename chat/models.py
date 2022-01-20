from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
import secrets

class ChatRoom(models.Model):
	room = models.CharField(max_length=200,blank=True)
	participant = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(null=True,blank=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.room

	def save(self, *args, **kwargs):
		self.date_created = timezone.now()
		super(ChatRoom, self).save(*args,**kwargs)

class Message(models.Model):
	room = models.CharField(max_length=200,blank=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	content = models.TextField()
	date_created = models.DateTimeField(null=True,blank=True)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return f'{self.sender.username} ({self.room})' 

	def save(self, *args, **kwargs):
		self.date_created = timezone.now()
		super(Message, self).save(*args,**kwargs)