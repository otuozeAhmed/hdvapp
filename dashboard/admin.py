from django.contrib import admin

from .models import Crane, Job, CraneModel, CraneLatestUpdate
from django.db import models

@admin.register(Crane)
class CraneAdmin(admin.ModelAdmin):
    model = Crane
    # ordering = ('name', 'design_capacity',)
    list_display = ['name', 'design_capacity', 'reg_no', 'image']
    list_filter = ['name', 'design_capacity', 'availability', 'fault_type', 'remark']
    search_fields = ['name', 'design_capacity', 'availability']


    
# @admin.register(CraneModel)
# class CraneAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description']
#     list_filter = ['name']
#     search_fields = ['name']
    

# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ['crane', 'job_num', 'job_description']
#     list_filter = ['crane', 'job_num']
#     search_fields = ['job_num']
    

# @admin.register(CraneLatestUpdate)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ['id','status']
#     list_filter = ['status']
    