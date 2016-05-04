from datetime import datetime
from models import Task
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def save_todo(request, *args, **kwargs):
    date = request.POST.get('date', datetime.today())
    time = request.POST.get('time', datetime.now().time())
    remark = request.POST['remark']
    reminder_type = request.POST.get('reminder_type', Task.SMS) # Default reminder will be SMS

    if not remark:
        return Response({'message': 'Remark not specified'}, status=status.HTTP_400_BAD_REQUEST)

    todo_task = Task.objects.create(date=date, time=time, remark=remark, reminder_type=reminder_type)

    return Response({'message': 'ToDo created successfully'}, status=status.HTTP_200_OK)