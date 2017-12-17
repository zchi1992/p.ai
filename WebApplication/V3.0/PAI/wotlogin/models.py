from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


# Create your models here.
class CatDisease(models.Model):
	disease = models.CharField(max_length=200)
	symptoms = models.CharField(max_length=200)
	introduction = models.CharField(max_length=2000)
	causes = models.CharField(max_length=2000)
	diagnosis = models.CharField(max_length=2000)
	treatment = models.CharField(max_length=2000)
	recovery = models.CharField(max_length=2000)
	cost = models.CharField(max_length=2000)
	def __str__(self):
		return self.disease

class Dic(models.Model):
	word = models.CharField(max_length=200)
	idx = models.IntegerField()

class CatEmbeddings(models.Model):
	row = models.CharField(max_length=200000)

class CatNce_weight(models.Model):
	row = models.CharField(max_length=200000)

class CatNce_bias(models.Model):
	row = models.CharField(max_length=200000)


class Pet(models.Model):
	user = models.ForeignKey(User)
	petname = models.CharField(max_length=100,null=True)
	pettype = models.CharField(max_length=100,null=True)
	petbreed = models.CharField(max_length=100,null=True)
	petbirthday = models.DateField(null=True)
	
class PetEvent(models.Model):
	pet = models.ForeignKey(Pet)
	eventtype = models.CharField(max_length=10000,null=True)
	discription = models.CharField(max_length=10000,null=True)
	action = models.CharField(max_length=10000,null=True)
	date = models.DateTimeField(null=True)
	#
	addedinfo = models.CharField(max_length=10000,null=True, blank = True)
	potentialinfo = models.CharField(max_length=10000,null=True)

class UserInfo(models.Model):
	user = models.ForeignKey(User, unique=True)
	currentpet = models.IntegerField()
	currentevent = models.IntegerField()