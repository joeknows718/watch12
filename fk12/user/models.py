from django.db import models
from django.contrib.auth.models import User
from flags.models import Flag, Plus1

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	verified_num = models.BooleanField(default=False)
	trust_score = models.PositiveSmallIntegerField(default=1)
	is_accepted = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True)
	date_verfied = models.DateTimeField(null=True, blank=True)
	last_active = models.DateTimeField(auto_now=True)
	flagged = models.BooleanField(default=False)
	date_locked = models.DateTimeField(null=True, blank=True)
	trusted = models.BooleanField(default=False)


	@classmethod
	def update_trust(self, *args, **kwargs):
		flags = Flag.objects.filter(account=self.id).count()
		pluses = Plus1.objects.filter(flagID.account=self.id).count()
		disputed = flags = Flag.objects.filter(account=self.id,disputed=True).count()
		if flags == 0:
			trust_score = 1
		if disputed == 0:
			trust_score = (1+pluses)/flags
		else:
			trust_score = ((1+pluses)/flags)/disputed

		self.trust_score = trust_score

		super(Account, self).save(*args, **kwargs)

	@classmethod
	def trust_check(self, *args, **kwargs):
		trust = self.trust_score
		if trust < .75:
			self.flagged = True

		super(Account, self).save(*args, **kwargs)

	@classmethod
	def reference_check(self, *args, **kwargs):

		if trusted_referall = Reference.objects.filter(refered=self.id,referer.flagged=False, referer.trusted=True).count():
			self.is_accepted = True 
			super(Account, self).save(*args, **kwargs)

		
		references = Reference.objects.filter(refered=self.id,referer.flagged=False).count()

		if references > 5:
			self.is_accepted = True 
			super(Account, self).save(*args, **kwargs)

		else:
			return False 

	def __str__(self):
		return self.user.username


class Reference(models.Model):
	refered = models.ManyToManyField(Account)
	referer = models.ManyToManyField(Account)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
        return self.referer.user.username + "-" + self.refered.user.username



