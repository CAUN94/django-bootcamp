from django.db import models

class Students(models.Model):
	name = models.CharField(max_length=45)
	clases = models.CharField(max_length=45)
	medals = models.CharField(max_length=45)
	year = models.IntegerField()
