from django.db import models

# Create your models here.
class Tracker(models.Model):
	timestamp_int = models.IntegerField()
	timestamp_str = models.CharField(max_length = 100)
	currency = models.CharField(max_length = 100)
	currency_value = models.DecimalField(max_digits=5, decimal_places=2)
