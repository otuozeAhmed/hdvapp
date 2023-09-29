from django.db import models

from datetime import timedelta
from django.db.models import DateTimeField
from django.urls import reverse

# class DateTruncMixin:

#     def truncate_date(self, dt):
#         return dt

#     def to_python(self, value):
#         value = super().to_python(value)
#         if value is not None:
#             return self.truncate_date(value)
#         return value

# class MinuteDateTimeField(DateTruncMixin, DateTimeField):
    
#     def truncate_date(self, dt):
#         return dt.replace(second=0, microsecond=0)

class CraneModel(models.Model):
    
    CRANE_CHOICES = (
        ('Terex Crane', 'Terex Crane'),
        ('Grove Crane', 'Grove Crane'),
        ('Locatelli Crane', 'Locatelli Crane'),
        ('Grove Yard Boss Crane', 'Grove Yard Boss Crane'),
        ('Grove Rough Terrain', 'Grove Rough Terrain'),
    )
    
    name = models.CharField(max_length=54, choices=CRANE_CHOICES, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Crane Categories'
        verbose_name_plural = 'Crane Categories'

class Crane(models.Model):

    
    AVAILABILITY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    # FAULT_TYPE = (
    #     ('Corrective', 'Corrective'),
    #     ('PMR', 'PMR'),
    #     ('Unavailable', 'Unavailable'),
    #     ('Not Specified', 'Not Specified'),
    #     ('None', 'None')
    # )
    
    # REMARKS = (
    #     ('Awaiting Spare', 'Awaiting Spare'),
    #     ('In progress', 'In Progress'),
    #     ('Good Condition', 'Good Condition'),
    #     ('Breakdown', 'Breakdown'),
    #     ('None', 'None')
    # )
    
    id = models.SmallAutoField(primary_key=True, null=False, blank=False)
    name = models.ForeignKey(CraneModel, on_delete=models.CASCADE, null=False, blank=False)
    reg_no = models.CharField(max_length=54, null=False, blank=False, editable = False)
    image = models.ImageField()
    about = models.TextField(null=False, blank=False)
    design_capacity = models.CharField(max_length=54, null=False, blank=False)
    availability = models.CharField(max_length=54, choices=AVAILABILITY, null=False, blank=False)
    fault_type = models.TextField(null=False, blank=False)
    remark = models.TextField(null=False, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    purchase_date = models.DateTimeField()
    
    def get_absolute_url(self):
        return reverse('crane_detail', kwargs={"pk": self.pk})
    
    
    def __str__(self) -> str:
        return str(self.name) + ' - ' + self.design_capacity
    
class Job(models.Model):
    id = models.SmallAutoField(primary_key=True, null=False, blank=False)
    crane = models.OneToOneField('Crane', on_delete=models.CASCADE, null=False, blank=False)
    job_num = models.CharField(max_length=54, null=False, blank=False)
    job_description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.job_num) + ' - ' + self.job_description
    
    class Meta:
        verbose_name = 'Associated Jobs'
        verbose_name_plural = 'Associated Jobs'

class CraneLatestUpdate(models.Model):
    
    STATUS = (
        ('Apply Update', 'Apply Updated Time'),
    )
    
    id = models.SmallAutoField(primary_key=True, null=False, blank=False)
    status = models.CharField(max_length=55, choices=STATUS, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Crane Update'
        verbose_name_plural = 'Apply Updates'
        
    def __str__(self):
        return str(self.updated_at)






