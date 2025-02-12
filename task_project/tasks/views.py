from django.shortcuts import render , redirect
from rest_framework import viewsets
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from .permissions import IsTaskAssignee
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer        

# Create a new user with a hashed password
user = User.objects.create_user(username="new_user", password="secure_pass123")
print(user.password)  # Outputs a hashed password


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Authentication successful!")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        return render(request, 'login.html')

# Restrict Views to Specific Roles


class TaskDetailView(APIView):

    permission_classes = [IsAuthenticated, IsTaskAssignee]

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        self.check_object_permissions(request, task)
        return Response({"title": task.title, "description": task.description})