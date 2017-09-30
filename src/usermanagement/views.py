from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def checkUsername(request):
    if request.GET.get('name', '') == '':
        flag = False
    else:
        flag = True
    return JsonResponse({'result': flag})

def checkUseremail(request):
    if request.GET.get('email', '') == '':
        flag = False
    else:
        flag = True
    return JsonResponse({'result': flag})
