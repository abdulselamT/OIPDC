from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Investor(models.Model):
	choices=(
		('Mr.','Mr.'),
		('Mrs.','Mrs.'),
		('Ms.','Ms.'),
		('Mx.','Mx.'),
		('Miss','Miss'),
		('Dr.','Dr.'),
		('Prof.','Prof.')
		)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=300,choices=choices,default=1)
	first_name=models.CharField(max_length=300)
	middle_name=models.CharField(max_length=300)
	last_name=models.CharField(max_length=300)
	gender=models.CharField(max_length=300)
	email=models.EmailField(max_length=300)
	phonenumber=models.CharField(max_length=300)
	education_level=models.CharField(max_length=300)
	current_Address=models.CharField(max_length=300)
	Tin=models.CharField(max_length=300)
	def __str__(self):
		return self.title + self.first_name

class DomesticRequest(models.Model):
	types=(
		('License','License'),
		('Land Request','Land Request'),
		('Expansion','Expansion'),
		)
	sectors=(
		('Manufacturing','Manufacturing'),
		('Agriculture','Agriculture'),
		('Service','Service'),
		)
	formchoice=(
		('soleprorietor','soleprorietor'),
		('PLC','PLC'),
		('joint-venture','joint-venture')
		)
	investor=models.ForeignKey(Investor,on_delete=models.CASCADE)
	form_of_investment=models.CharField(max_length=300,choices=formchoice)
	requested_type=models.CharField(max_length=300,choices=types)
	requested_land=models.FloatField()
	sector=models.CharField(max_length=300,choices=sectors)
	project_name=models.CharField(max_length=300)
	project_description=models.TextField(max_length=300)
	capital=models.FloatField()
	owner_equity=models.FloatField()
	bank_loan=models.FloatField()
	temporay_job=models.CharField(max_length=300)
	Permanent_job=models.CharField(max_length=300)
	def __str__(self):
		return self.form_of_investment

class FileInfo(models.Model):
	investor=models.ForeignKey(Investor,on_delete=models.CASCADE)
	proposal=models.FileField()
	passport=models.FileField()
	memorendum=models.FileField()
	bank_statement=models.FileField()
	id_card=models.FileField()
	power_of_attorney=models.FileField(null=True,blank=True)
