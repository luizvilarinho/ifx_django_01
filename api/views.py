import response as response
from django.urls import path, include
from rest_framework.decorators import api_view
from .models import Book, DbUModel, Course
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import BookSerializer, ModelSerializer, CourseSerializer, CollectionSerializer

#departaments table
from departaments.models import DbDModel, Employee, Company
from departaments.serializer import CompanySerializer, EmployeeSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = DbUModel.objects.all()
    serializer_class = ModelSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@api_view(['GET'])
def collectionViewSet(request):
    book = Book.objects.all()
    course = Course.objects.all()
    umodel = DbUModel.objects.all()

    #dbDmodel = DbDModel.objects.all()
    company = Company.objects.all()
    employee = Employee.objects.all()

    serializeBookObj = BookSerializer(book, many=True)
    serializeCourseObj = CourseSerializer(course, many=True)
    serializeModelUObj = ModelSerializer(umodel, many=True)

    #serializeDbDModelObj = ModelSerializer(book, many=True)
    serializeEMployeeObj = EmployeeSerializer(employee, many=True)
    serializeCompanyObj = CompanySerializer(company, many=True)

    #result = serializeBookObj.data + serializeCourseObj.data + serializeModelUObj.data

    #logic goes here
    idsBooks = int(0)
    idsModels = int(0)
    idsCourses = int(0)

    for e in serializeBookObj.data:
        idsBooks = idsBooks + int(e['id'])

    for i in serializeModelUObj.data:
        idsModels = idsModels + int(i['id'])

    for j in serializeCourseObj.data:
        idsCourses = idsCourses + int(j['id'])

    ids_soma = idsBooks + idsModels + idsCourses

    result = {
        'soma_ids': ids_soma,
        'success': True,
        'books': serializeBookObj.data,
        'courses': serializeCourseObj.data,
        'users': serializeModelUObj.data,
        'companys': serializeCompanyObj.data,
        'employees': serializeEMployeeObj.data,
        #'departaments': serializeDbDModelObj,
    }
    return Response(result)


# @api_view()
# def collection(request):
#     # books = requests.get("http://localhost:8000/books")
#     debUModel = requests.get("http://localhost:8000/models")
#     courses = requests.get("http://localhost:8000/courses")
#     # books = json.loads(books.content)
#
#     books =
#     print(books)
#     debUModel = json.loads(debUModel.content)
#     courses = json.loads(courses.content)
#
#     #ids_soma = int(books[0]['id']) + int(debUModel[0]['id']) + int(courses[0]['id'])
#     idsBooks = int(0)
#     idsModels = int(0)
#     idsCourses = int(0)
#
#     for e in books:
#         idsBooks = idsBooks + int(e['id'])
#
#     for i in debUModel:
#         idsModels = idsModels + int(i['id'])
#
#     for j in courses:
#         idsCourses = idsCourses + int(j['id'])
#
#     ids_soma = idsBooks + idsModels + idsCourses
#     #[v1, v2] = [request.query_params['valor1'], request.query_params['valor2']]
#     #soma = int(v1) + int(v2)
#     # print(users)
#
#     return Response({"success": True, "ids_soma": ids_soma, "books": books, "debUModel": debUModel, "courses": courses,})
