from django.shortcuts import render
from . models import TaskModel
from . serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import  IsAuthenticated

class TaskViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TaskModel.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('completed',)
    ordering = ('-date_created',)
    search_fields = ('task_name',)

'''
class DueTaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializer
class CompletedTaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializer
    
'''
