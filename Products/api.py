from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (
    ProductSerializer, ProductModelSerializer,
    CategoryModelSerializer,
    CommentModelSerializer
)
from .models import Product, Brand, Category, Comment


@csrf_exempt
def product_list(request):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have POST and GET is one function
    '''
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        # !!!attention: did not add 'data=' befor the "products" , becuse we are not give them data we just wanth get them
        # many=True means this is a several item and not one object, return an array of objects
        return JsonResponse(serializer.data, safe=False)
        # serializer.data meanse change the format of serializer from array to object
        # safe=False should be, it means you sey to django i now it is array and array not safe but you process that
    if request.method == "POST":
        data = JSONParser().parse(request)
        # hear we get data from request and converting json to dictionary
        serializer = ProductModelSerializer(data=data)
        # !!!attention: did not forget add 'data=' befor the "data"

        if serializer.is_valid():
            serializer.save()
             # hear we call create func we write befor in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have GET, PUT, DELETE is one function
    '''
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductModelSerializer(product)
        return JsonResponse(serializer.data, safe=True)
        # safe should be true becuse in hear we have just one json file and not an array
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductModelSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse(status=204)


@csrf_exempt
def category_list(request):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have POST and GET is one function
    '''
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        # !!!attention: did not add 'data=' befor the "products" , becuse we are not give them data we just wanth get them
        # many=True means this is a several item and not one object, return an array of objects
        return JsonResponse(serializer.data, safe=False)
        # serializer.data meanse change the format of serializer from array to object
        # safe=False should be, it means you sey to django i now it is array and array not safe but you process that
    if request.method == "POST":
        data = JSONParser().parse(request)
        # hear we get data from request and converting json to dictionary
        serializer = CategoryModelSerializer(data=data)
        # !!!attention: did not forget add 'data=' befor the "data"
        if serializer.is_valid():
            serializer.save()
             # hear we call create func we write befor in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have GET, PUT, DELETE is one function
    '''
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategoryModelSerializer(category)
        return JsonResponse(serializer.data, safe=True)
        # safe should be true becuse in hear we have just one json file and not an array
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoryModelSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def comments_list(request):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have POST and GET is one function
    '''
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentModelSerializer(comments, many=True)
        # !!!attention: did not add 'data=' befor the "products" , becuse we are not give them data we just wanth get them
        # many=True means this is a several item and not one object, return an array of objects
        return JsonResponse(serializer.data, safe=False)
        # serializer.data meanse change the format of serializer from array to object
        # safe=False should be, it means you sey to django i now it is array and array not safe but you process that
    if request.method == "POST":
        data = JSONParser().parse(request)
        # hear we get data from request and converting json to dictionary
        serializer = CommentModelSerializer(data=data)
        # !!!attention: did not forget add 'data=' befor the "data"
        if serializer.is_valid():
            serializer.save()
             # hear we call create func we write befor in serializer class
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def comment_detail(request, pk):
    '''
    in rest_framework we are not create a several view for delete, update, get and any one else
    for list we have GET, PUT, DELETE is one function
    '''
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CommentModelSerializer(comment)
        return JsonResponse(serializer.data, safe=True)
        # safe should be true becuse in hear we have just one json file and not an array
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentModelSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        comment.delete()
        return HttpResponse(status=204)

