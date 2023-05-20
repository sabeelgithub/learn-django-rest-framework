from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    students = Student.objects.all()
    
    serializer = StudentSerializer(students, many=True)
    return Response({"status":200,"payload":serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    print(data)
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
    
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':'you sent'})

