from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

class TodoList(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)
class TodoDetail(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request,id):
        todo=Todo.objects.get(id=id)
        serializer=TodoSerializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,id):
        todo=Todo.objects.get(id=id) 
        serializer=TodoSerializer(todo,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,id):
        todo=Todo.objects.get(id=id) 
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
   




