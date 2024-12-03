from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(APIView):
    serializer_class = TaskSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=200)
            except Task.DoesNotExist:
                return Response({'message': 'Task not found'}, status=404)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=200)


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found'}, status=404)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({'message': 'Task deleted'}, status=204)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found'}, status=404)
