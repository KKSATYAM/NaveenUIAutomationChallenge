from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.generic import View
from testapp.models import Employee
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDetail(View):

    def get(self,request,*args,**kwagrs):
        emp_obj=Employee.objects.all();

        json_data=serialize('json',emp_obj)
        

        return HttpResponse(json_data,status=200)
    
    
    def post(self,request,*args,**kwagrs):
        emp_obj=Employee.objects.all();
        json_data=serialize('json',emp_obj)
        return HttpResponse(json_data,status=200)
    




