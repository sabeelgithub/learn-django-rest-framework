from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics

# Create your views here.
class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"




@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_books(request):
     print(request.user)
     books = Book.objects.all()
     serializer = BookSerializer(books,many=True)
     return Response({'status':200,'payload':serializer.data,'message':'these are the books'})


class RegisterAPI(APIView):
    try:
        def post(self,request):
            serializer = RegisterSerializer(data=request.data)
            print(serializer,'onnnnnnnnnnnnneeeeeeeeee')
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            print(user,'uuuuuuuuuseeeeeeeeeeeeeeeer')
            # token_obj,_ = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            print(refresh,'Tooooooooken')
            print(str(refresh))
            return Response({'status':200,'payload':serializer.data,'refresh':str(refresh),'access':str(refresh.access_token),'message':'registerd and your token is above'})
    except Exception as e:
        print(e)
     


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(authentication_classes,'1111')
        print(permission_classes,'222222')
        return Response({'status':200,'payload':serializer.data})
    def post(self,request):
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

    def put(self,request):
        try:
            print('oneeee')
            
            student = Student.objects.get(id=request.data['id'])
            print(student,'jum')
            serializer = StudentSerializer(student,request.data,partial=True)
            print(serializer)
            print('modaaaa')
            if not serializer.is_valid():
                print('nooooooooooooot vaaaaaaaaaalid')
                return Response({'status':404,'error':serializer.errors,'message':'something went wrong'})
            
            serializer.save()
            print('saaaaaaaaaaaved')
            return Response({'sataus':200,'payload':serializer.data,'message':'updated'})
        except Exception as e:
            print(e,'thett')
            return Response({'status':403,'message':e})

    def patch(self,request):
        id = request.data['id']
        try:
            print('oneeee')
            
            student = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student,request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':404,'error':serializer.errors,'message':'something went wrong'})
            
            serializer.save()
            return Response({'sataus':200,'payload':serializer.data,'message':'updated'})
        except Exception as e:
            print(e,'thett')
            id = request.data['id']
            return Response({'status':403,'message':f'id {id} is invalid'})

    def delete(self,request):
        
        try:
            id = request.data['id']
            student = Student.objects.get(id=request.data['id'])
            koi = student
            delete_id = koi.id
            print(koi.id)
            student.delete()
            print(koi,'after')
            print(koi.id,'afttttttttttttttttter')
            return Response({'status':200,'message':f'id {id} deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'id is invalid'})
     


# @api_view(['GET'])
# def home(request):
#     students = Student.objects.all()
    
#     serializer = StudentSerializer(students, many=True)
#     return Response({'status':200,'payload':serializer.data})

# @api_view(['POST'])
# def post_student(request):
   
#         new = request.data
#         print(new,'evideeeeeeeeeee')
#         print(request.data,'modeeeeeenooooooo')
#         serializer = StudentSerializer(data=new)
#         print(serializer,'seeeeeeeeeeeeeri')
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        
#         serializer.save()
#         return Response({'status':200,'payload':serializer.data,'message':'you sent'})

# @api_view(['PUT'])
# def update_student(request,id):
#     try:
#         print('oneeee')
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student,request.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'status':404,'error':serializer.errors,'message':'something went wrong'})
        
#         serializer.save()
#         return Response({'sataus':200,'payload':serializer.data,'message':'updated'})
#     except Exception as e:
#          print(e,'thett')
#          return Response({'status':403,'message':e})

# @api_view(['DELETE'])    
# def delete_student(request,id):
#      try:
#           student = Student.objects.get(id=id)
#           koi = student
#           delete_id = koi.id
#           print(koi.id)
#           student.delete()
#           print(koi,'after')
#           print(koi.id,'afttttttttttttttttter')
#           return Response({'status':200,'message':f'id {id} deleted'})
#      except Exception as e:
#           print(e)
#           return Response({'status':403,'message':f'id {id} is invalid'})
          
          

     
 

