from django.urls import path
from app1 import views

urlpatterns = [
	path('home/',views.home,name='home'),
	path('login/',views.login,name='login'),
	path('register/',views.register,name='register'),
	path('logout/',views.logout,name='logout'),
]
