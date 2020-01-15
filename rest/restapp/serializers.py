from . models import TaskModel
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = TaskModel
        fields = ('id','task_name','task_desc','date_created','completed','image')
