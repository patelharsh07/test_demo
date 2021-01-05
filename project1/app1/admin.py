from django.contrib import admin
from .models import UserTypeMaster,UserMaster
# class UserAdmin(admin.ModelAdmin):
# 	list_display=['UserName','UserPassword']
# 	list_filter=['UserEmail','UserName']
# 	search_fields=['UserPassword','UserEmail']
# 	ordering=['UserName','UserPassword']
# Register your models here.
ModelField=lambda model: type('Subclass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],
	})
admin.site.register(UserMaster,ModelField(UserMaster))
admin.site.register(UserTypeMaster,ModelField(UserTypeMaster))

# admin.site.register(UserTypeMaster)
# admin.site.register(UserMaster,UserAdmin)
