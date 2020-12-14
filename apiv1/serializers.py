from rest_framework import serializers
from depts.models import Depts

class DeptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depts
        fields = ['id','deploy_name','created_at']