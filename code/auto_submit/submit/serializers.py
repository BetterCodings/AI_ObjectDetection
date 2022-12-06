from rest_framework import  serializers
from .models import Lecture,Class,Attendence,Student,Attendence_Student

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('ID', 'subject','pID',"sum")


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('day', 'period','lID',"classroom")

# class AttendenceSerializer(serializers.ModelSerializer):
#     image=serializers.ImageField(use_url=True)
#     class Meta:
#         model = Attendence
#         fields = ('date', 'lID','attend',"image")

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ('date', 'lID','attend')
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('ID',"name")
        
class Attendence_StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence_Student
        fields = ('aID',"sID","submit")
