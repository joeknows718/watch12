from django.db import models
from user.models import Account
# Create your models here.

class Flag(models.Model):
	title = models.Charfield(max_length=150)
	account = models.ForeignKey(Account, related_name='flags')
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lon = models.DecimalField(max_digits=9, decimal_places=6)
	notes = models.Charfield(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	disputed = models.BooleanField(default=False)
	presict = models.Charfield(max_length=150)
	badge_num = models.PositiveSmallIntegerField(null=True, blank=True)
	active = models.BooleanField(default=True)

	#need fn to deactive old ones. 

	def __str__(self):
		return self.title

class Plus1(models.Model):
		flagID = models.ForeignKey(Flag, related_name=pluses)
		userID = models.ForeignKey(Account, related_name, related_name='plused')
		date = models.DateTimeField(auto_now_add=True)

class Comment(model.Model):
	commenter = models.ForeignKey(Account, related_name="commenter")
	text = models.Charfield(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	flagID = model.ForeignKey(Flag)

	def __str__(self):
		return "Comment for" + self.flagID.title

class Img(models.Model):
	flag =  models.ForeignKey(Flag related_name='imgs')
	img = models.ImageField(upload_to='media/flags')
	
	def __str__(self):
		return "Image for" + self.flagID.title

class Dispute(models.Model):
	account = models.ForeignKey(Account, related_name="dispute")
	flag = models.ForeignKey(Flag related_name='disputes')
	date = models.DateTimeField(auto_now_add=True)


