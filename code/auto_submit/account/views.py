from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser


from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer


class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# @csrf_exempt
# def account_list(request):
#     if request.method == 'GET':
#         query_set = Account.objects.all()
#         serializer = AccountSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AccountSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def account(request, pk):
#     obj = Account.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = AccountSerializer(obj)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AccountSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         obj.delete()
#         return HttpResponse(status=204)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_ID = data['ID']
        obj = Account.objects.get(ID=search_ID)

        if data['passwd'] == obj.passwd:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
