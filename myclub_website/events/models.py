from django.db import models


class Venue(models.Model):
	name = models.CharField('Venue Name',max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Code',max_length=15)
	phone = models.CharField('Contact Phone',max_length=11)
	web =  models.URLField('Website address')
	email_address = models.EmailField('Email address')

	def __str__(self):
		return self.name


class Event(models.Model):
	name = models.CharField('Event name',max_length=120)
	event_date = models.DateTimeField('Event Date')
	#venue = models.CharField(max_length=120)
	venue = models.ForeignKey(Venue, blank=True, null=True)
	manager = models.CharField(max_length=60)
	description = models.TextField(blank=True)


	def __str__(self):
		return self.name