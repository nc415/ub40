from django.db import models
from django.conf.urls import patterns, include, url
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User
import random
import string
from django.core.exceptions import ValidationError
# Create your models here.
class Company(models.Model):


	Company_Name = models.CharField(max_length=128, null=False)
	Company_Region = models.CharField(max_length=128, blank=True)
	Company_Id = models.SlugField(blank=True, unique=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse('page-title', kwargs={'pk': self.pk})


	def save(self, *args, **kwargs):
		
		
		super(Company, self).save(*args, **kwargs)

	def __str__(self):
		return self.Company_Name

class BU(models.Model):

	Parent_Company=models.ForeignKey(Company, default=0, related_name='units')
	BU_Name=models.CharField(max_length=128, null=False)
	def __str__(self):
		return self.BU_Name
class Year(models.Model):

	Year = models.CharField(max_length=128, null=False)

	def save(self, *args, **kwargs):
		
		
		super(Year, self).save(*args, **kwargs)

	def __str__(self):
		return self.Year

class PLtype(models.Model):
	element = models.CharField(max_length=128, null=False)
	def save(self, *args, **kwargs):
		
		
		super(PLtype, self).save(*args, **kwargs)

	def __str__(self):
		return self.element

class PLstandard(models.Model):
	Company_Name=models.ForeignKey(Company, default=0, related_name='Company')
	BU=models.ForeignKey(BU, default=0, related_name='BU')
	Year=models.ForeignKey(Year, default=0, related_name='years')
	PLtype=models.ForeignKey(PLtype, default=0, related_name='PLType')
	TotalRevenue = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	SalesofElectricityandGas = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	OtherRevenue = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	TotalOperatingCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	DirectFuelCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	DirectCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	NetworkCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	EnvironmentalAndSocialCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	OtherDirectCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False,default=0)
	IndirectCosts = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	WACOFEG = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	EBITDA = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	DA = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	EBIT = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	Volume = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)
	AverageCustomersPerSite = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0)