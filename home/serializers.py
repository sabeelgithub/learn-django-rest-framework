from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id',]
        fields = '__all__'
    
    def validate(self,data):
        if data['age']:
            if data['age'] < 17:
                raise serializers.ValidationError({'error':'age cant be less than 17'})
        
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
        
        if data['father_name']:
            for i in data['father_name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
                
        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

