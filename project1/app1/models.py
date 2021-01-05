from django.db import models

# Create your models here.
class UserTypeMaster(models.Model):
	UserTypeID=models.AutoField(primary_key=True)
	UserType=models.CharField(max_length=255,blank=False)
	CreateAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)

	def __str__(self):
		return self.UserType

class UserMaster(models.Model):
	UserID=models.AutoField(primary_key=True)
	UserName=models.CharField(max_length=25,help_text='Enter User Name: ',null=False, blank=False)
	UserTypeID=models.ForeignKey(UserTypeMaster,null=True,on_delete=models.SET_NULL)
	UserPassword=models.CharField(max_length=20,blank=False)
	UserEmail=models.EmailField(max_length=25,unique=True)
	UserMobile=models.BigIntegerField(blank=False)
	UserAddress=models.CharField(max_length=255,null=True,blank=True,default='None')
	CreateAt=models.DateTimeField(auto_now_add=True)
	ModifiedAt=models.DateTimeField(auto_now=True)
	IsActive=models.BooleanField(default=0)

	class Meta:
		ordering=['UserName']

	def get_absolute_url(self):
		return reverse('models-details-view', args=[str(self.id)])

	def __str__(self):
		return self.UserName