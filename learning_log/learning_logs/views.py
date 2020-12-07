from django.shortcuts import render
from django.http import JsonResponse,HttpRequest
from .models import Book
from django.core import serializers
import json


# from .models import Topic

# Create your views here.
# def index(request):
#     """学习笔记的主页"""
#     return render(request,'learning_logs/index.html')
#
#
# def topics(request):
#
#     """显示所有的主题"""
#     topics = Topic.order_by('date_added')
#     context = {'topics':topics}
#     return render(request,'learning_logs/topics.html',context)

# 新增两个接口

# @require_http_methods(['get'])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# @require_http_methods(['get'])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
