from django.db import models
from django_bleach.models import BleachField
from .utils import generate_api_key

class Quote(models.Model):
	FACULTY = 'FAC'
	GRAD_STUDENT = 'GS'
	INVITED_SPEAKER = 'INV'
	OTHER = 'OTH'
	SPEAKER_CLASS_CHOICES = (
			(FACULTY, "Faculty"),
			(GRAD_STUDENT, "Graduate Student"),
			(INVITED_SPEAKER, "Invited Speaker"),
			(OTHER, "Other"),
			)
	
	date = models.DateField()
	speaker = models.CharField(max_length=100)
	speaker_class = models.CharField(max_length=3, choices=SPEAKER_CLASS_CHOICES,
			default=FACULTY, blank=False)
	quotation = BleachField()
	context = models.CharField(max_length=256,blank=True)
	approved = models.BooleanField(default=False)
	votes = models.SmallIntegerField(default=0)

	def __unicode__(self):
		return unicode(self.quotation) + u" - " + unicode(self.speaker)

	def get_fields_dict(self):
		return {'date' : self.date,
				'speaker' : self.speaker,
				'speaker_class' : self.speaker_class,
				'quotation' : self.quotation,
				'context' : self.context,
				'votes' : self.votes}

	class Meta:
		ordering = ["-date"]

class ApiUserManager(models.Manager):
	def get_unique_key(self):
		new_key = generate_api_key()
		while(self.get_queryset().filter(api_key=new_key).exists()):
			new_key = generate_api_key()
		return new_key

class ApiUser(models.Model):
	name = models.CharField(max_length=100)
	api_key = models.CharField("API key", max_length=64, unique=True)
	key_expires = models.DateField()

	objects = ApiUserManager()

	def __unicode__(self):
		return u'API User: ' + unicode(self.name)

	class Meta:
		verbose_name = "API user"
