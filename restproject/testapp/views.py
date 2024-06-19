from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from testapp.models import EmployeeModel
from testapp.seralizer import EmployeeSerializer

# # class TestAPIView(APIView):

#     def get(self,request,*args,**kwargs):
#         return Response({'msg':'GET-REQUEST Good Morning!!'})
    
#     def post(self,request,*args,**kwargs):
#         return Response({'msg':'POST-REQUEST Good Morning!!'})
    
#     def put(self,request,*args,**kwargs):
#         return Response({'msg':'PUT-REQUEST Good Morning!!'})
    
#     def patch(self,request,*args,**kwargs):
#         return Response({'msg':'PATCH-REQUEST Good Morning!!'})
    
#     def delete(self,request,*args,**kwargs):
#         return Response({'msg':'DELETE-REQUEST Good Morning!!'})

class EmployeeListCreateView(RetrieveUpdateDestroyAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer
    # lookup_field='id'
    

    



