from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=45)
	description = models.TextField()
	release_date = models.DateField()
	duration = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Wizard(models.Model):
	name = models.CharField(max_length=45)
	house = models.CharField(max_length=45)
	pet = models.CharField(max_length=45)
	year = models.IntegerField()
