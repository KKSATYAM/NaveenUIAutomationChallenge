from rest_framework.serializers import ModelSerializer
from testapp.models import EmployeeModel

class EmployeeSerializer(ModelSerializer):

    class Meta:
        model=EmployeeModel
        # exclude=['id',]
        fields='__all__'
        
