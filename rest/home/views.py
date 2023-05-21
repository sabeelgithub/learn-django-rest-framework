from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_books(request):
     books = Book.objects.all()
     serializer = BookSerializer(books,many=True)
     return Response({'status':200,'payload':serializer.data,'message':'these are the books'})
     


@api_view(['GET'])
def home(request):
    students = Student.objects.all()
    
    serializer = StudentSerializer(students, many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
   
        new = request.data
        print(new,'evideeeeeeeeeee')
        print(request.data,'modeeeeeenooooooo')
        serializer = StudentSerializer(data=new)
        print(serializer,'seeeeeeeeeeeeeri')
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'you sent'})

@api_view(['PUT'])
def update_student(request,id):
    try:
        print('oneeee')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,request.data,partial=True)
        if not serializer.is_valid():
            return Response({'status':404,'error':serializer.errors,'message':'something went wrong'})
        
        serializer.save()
        return Response({'sataus':200,'payload':serializer.data,'message':'updated'})
    except Exception as e:
         print(e,'thett')
         return Response({'status':403,'message':e})

@api_view(['DELETE'])    
def delete_student(request,id):
     try:
          student = Student.objects.get(id=id)
          koi = student
          delete_id = koi.id
          print(koi.id)
          student.delete()
          print(koi,'after')
          print(koi.id,'afttttttttttttttttter')
          return Response({'status':200,'message':f'id {id} deleted'})
     except Exception as e:
          print(e)
          return Response({'status':403,'message':f'id {id} is invalid'})
          
          

     
 

