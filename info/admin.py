from django.contrib import admin
from info.models import Students
class Students(admin.ModelAdmin):
	admin.site.register(Students)