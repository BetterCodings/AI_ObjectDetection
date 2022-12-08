
import numpy as np
import cv2

from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from submit.models import Class,Lecture,Attendence,Student,Attendence_Student,Posts
from .serializers import ClassSerializer,LectureSerializer,AttendenceSerializer,StudentSerializer,Attendence_StudentSerializer,PostsSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime
from rest_framework.parsers import JSONParser
import os
from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.response import Response
from submit.funtion import yolo,setimage
from django.core.files.base import ContentFile
from auto_submit.settings import MEDIA_URL

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
    def create(self, request, *args, **kwargs):
        data=request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        _,results=yolo("media/"+str(request.data["image"]))
        setimage("media/"+str(request.data["image"]),results)
        headers = self.get_success_headers(serializer.data)

        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostsViewset(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        #assert False,serializer["image"].url
        #yolo(serializer["image"].url)
        yolo("media/"+str(request.data["image"]))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def create(self, request, *args, **kwargs):

    #     # post_data = request.data
    #     # fileObj = request.FILES['image']
        
    #     # file_name = str(request.FILES['image']).split('.')
    #     # file_name = file_name[0]
    #     # fs = FileSystemStorage() 
    #     # filePathName = fs.save(fileObj.name, fileObj)
    #     # filePathName = fs.url(filePathName)
    #     # testimage = '.' + filePathName
    #     # assert False,testimage
    #     # #img = load_img(testimage)
    #     # #directory = os.path.join(os.getcwd(), 'submit/images' + os.sep)  # + os.sep 이거 붙여줘야함
    #     # #img.save(directory + file_name+'.jpg')
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # p=Posts.objects.get(ID=request.data["ID"])
    #     # image = cv2.imencode('.jpg', p.image.read())
    #     # x,y,w,h = 50,50,100,100
    #     # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0))
    #     # file = ContentFile(image)
    #     # p.image.save('myphoto.jpg', file, save=True)
        
    #     # assert False,MEDIA_URL

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            
        
# Create your views here.
    # def create(self, request): 
    #     post_data = request.data
    #     fileObj = request.FILES['image']  # 파일 이름을 받는다. [필드명]
    #     file_name = str(request.FILES['image']).split('.')  # 이름 추출을 위해 확장자를 제거해줬다.
    #     file_name = file_name[0]
    #     fs = FileSystemStorage()  # 이 메소드를 위해 해당 라이브러리 import 한다.
    #     filePathName = fs.save(fileObj.name, fileObj)
    #     filePathName = fs.url(filePathName)
    #     testimage = '.' + filePathName
    #     img = load_img(testimage)  # 저기서 media 폴더에 저장되기 이전에 채온 이미지를 불러와서 image라는 폴더에 저장했다.
    #     directory = os.path.join(os.getcwd(), 'bg_removal/images' + os.sep)  # + os.sep 이거 붙여줘야함
    #     img.save(directory + file_name+'.jpg')
    

@csrf_exempt
def Posts_(request):
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        # search_lID = data['ID']
        # search_date = data['image']
        search_lID = request['ID']
        search_date = request['image']
        attendence = Attendence.objects.get(lID=search_lID,date=search_date)
        serializer = PostsSerializer(attendence,many=True)
        return JsonResponse(serializer.data, safe=False)

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
