from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from submit.models import Class,Lecture,Attendence,Student,Attendence_Student
from .serializers import ClassSerializer,LectureSerializer,AttendenceSerializer,StudentSerializer,Attendence_StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime
from rest_framework.parsers import JSONParser
# Create your views here.

# @api_view(['GET'])
# def get_api(request):
#     posts = Post.objects.all()
#     serailized_posts= PostSerializer(posts, many=True)
#     return Response(serailized_posts.data)

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassViewset(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
class LectureViewset(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    
class AttendenceViewset(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer

@csrf_exempt
def lecture(request, ID):
    if request.method == 'GET':
        lecture = Lecture.objects.get(ID=ID)
        serializer = LectureSerializer(lecture)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def today_class(request, pID):
    if request.method == 'GET':
        Lecture_set = Lecture.objects.filter(pID=pID)
        result=[]
        for lecture in Lecture_set:
            class_=lecture.class_set.filter(lID=lecture.ID,day=datetime.today().weekday())
            result= result + list(class_)
        serializer = ClassSerializer(result,many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def class_(request, pID):
    if request.method == 'GET':
        Lecture_set = Lecture.objects.filter(pID=pID)
        result=[]
        for lecture in Lecture_set:
            class_=lecture.class_set.filter(lID=lecture.ID)
            result= result + list(class_)
        serializer = ClassSerializer(result,many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def lecture_student(request, ID):
    if request.method == 'GET':
        lecture = Lecture.objects.get(ID=ID)
        serializer = StudentSerializer(lecture.members.all(),many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def select_attendence(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_lID = data['lID']
        search_date = data['date']
        result = Attendence.objects.get(lID=search_lID,date=search_date)
        serializer = AttendenceSerializer(result)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def update_attendence(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AttendenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            search_lID = data['lID']
            search_date = data['date']
            result = Attendence.objects.get(lID=search_lID,date=search_date)
            result.init_Attendence_Student()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        search_lID = data['lID']
        search_date = data['date']
        attendence = Attendence.objects.get(lID=search_lID,date=search_date)
        serializer = Attendence_StudentSerializer(attendence, data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def student(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_lID = data['lID']
        search_date = data['date']
        attendence = Attendence.objects.get(lID=search_lID,date=search_date)
        a_s=Attendence_Student.objects.filter(aID=attendence)
        serializer = Attendence_StudentSerializer(a_s,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        search_sID = data['sID']
        search_aID = data['aID']
        a_s=Attendence_Student.objects.get(aID=search_aID,sID=search_sID)
        serializer = Attendence_StudentSerializer(a_s, data=data)
        if serializer.is_valid():
            serializer.save()
            attendence=Attendence.objects.get(id=search_aID)
            attendence.set_count()
            
        return JsonResponse(serializer.data, safe=False)
