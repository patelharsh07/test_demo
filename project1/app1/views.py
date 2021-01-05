from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserMaster,UserTypeMaster
from .forms import LoginForms,RegisterForms
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def home(request):
	context={}
	if 'login' in request.session:
		useremail=request.session['user']
		return render(request,'base.html',context={'useremail':useremail})
	else:
		return redirect('login')

	data1=UserMaster.objects.all()
	print('data1:',data1)
	data2=UserMaster.objects.filter(UserTypeID=1).values()
	print('data2:',data2)
	data3=UserMaster.objects.filter(UserTypeID__Usertype='student').values()
	print('data3:',data3)
	data4=UserMaster.objects.filter(UserTypeID=1).values()
	print('data4:',data4)
	data5=UserMaster.objects.filter(UserTypeID=1).values('UserName','UserTypeID__Usertype')
	print('data5:',data5)
	data6=UserMaster.objects.filter(UserTypeID=1).values('UserName','UserTypeID__Usertype')[0]['UserName'].split('r')[0]
	print('data6:',data6)
	return render(request,'base.html',context={'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6})
def login(request):
	context={}
	if not 'login' in request.session:
		msg=''
		form=LoginForms(request.POST or None)
		context['form']=form
		if request.POST:
			if UserMaster.objects.filter(UserEmail=request.POST['UserEmail'],UserPassword=request.POST['UserPassword']).exists():
				request.session['login']=True
				request.session['user']=request.POST['UserEmail']
				return redirect('home')
				# return render(request,'base.html')
			else:
				msg=form.error
				context['msg']=msg
		return render(request,'login.html',context={'form':form,'msg':msg})
	else:
		useremail=request.session['user']
		return render(request,'base.html',context={'useremail':useremail})
		# return redirect('home',context)
def register(request):
	reg_form=RegisterForms(request.POST)
	print('form',reg_form)
	if request.POST:
		if not UserMaster.objects.filter(UserEmail=request.POST['UserEmail']).exists():
			data7=UserMaster.objects.create(UserName=request.POST['UserName'],UserPassword=request.POST['UserPassword'],UserMobile=request.POST['UserMobile'],UserEmail=request.POST['UserEmail'])
			return render(request,'base.html')
	return render(request,'register.html',context={'reg_form':reg_form})

class ViewUser(APIView):
	def post(self,request):
		UserData=UserMaster.objects.all().values()
		return Response({'response':UserData})
def logout(request):
	del request.session['login']
	del request.session['User']
	return redirect('login')