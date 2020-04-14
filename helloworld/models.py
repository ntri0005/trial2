from django.db import models

# Create your models here.

class HospitalTable(models.Model):
	hospital_id = models.PositiveIntegerField()
	hospital_name = models.TextField()
	hospital_address = models.TextField()
	hospital_wt = models.FloatField()
	hospital_latitude = models.FloatField()
	hospital_longitude = models.FloatField()
	
class BeachTable(models.Model):
	beach_id = models.PositiveIntegerField()
	beach_name = models.TextField()
	beach_latitude = models.FloatField()
	beach_longitude = models.FloatField()
	


class trialTable(models.Model):
	trialtable_title = models.CharField(max_length=200)
	trialtable_content = models.TextField()
	trialtable_published = models.DateTimeField("date published")
	
	def __str__(self):
		return self.trialtable_title