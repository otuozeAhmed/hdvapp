from django.shortcuts import get_object_or_404, render, redirect
from django.views import View, generic

from .models import Crane, Job, CraneModel, CraneLatestUpdate
from datetime import datetime

from django.conf import settings  
from django.conf.urls.static import static  


# class HDVCategory(View):
    
    # template_name = "hdv_category.html"
    
    # def get(self, request, *args, **kwargs):
    #     qs = CraneModel.objects.all()
    #     context = {
    #         'qs': qs
    #     }
    #     return render(request, self.template_name, context) 
    

# class HDVCategoryDetails(View):
    
    # template_name = "hdv_category_details.html"
    
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'test': 'test'
    #     }
    #     return render(request, self.template_name, context) 
    


class HDVDashboardView(View):
    
    template_name = "dashboard_view.html"
    
    # def __init__(self, primary_key):
    #     self.crane_update = get_object_or_404(CraneLatestUpdate, pk=primary_key)
        
    
    def get(self, request, *args, **kwargs):
        qs = Crane.objects.all()
        now = datetime.now()
        context = {
            'qs': qs,
            'time': now
        }
       
        return render(request, self.template_name, context)
    
    
    

class CraneDetail(generic.DetailView):
    
    model = Crane
    template_name = "crane_detail.html"
    context_object_name = 'crane'
    
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'test': 'test'
    #     }
    #     return render(request, self.template_name, context) 


    
def sample_page(request):
    return render(request, 'home.html')





def error_page(request):
    return render(request, 'page-404.html')


