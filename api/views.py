from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from task.models import Task
from api.serializers import TaskSerializer
from api.permissions import IsOwnerOrReadOnly

class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class TaskList(TaskMixin, ListCreateAPIView):
	pass

class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
	pass
    
