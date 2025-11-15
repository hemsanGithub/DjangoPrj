from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# Model object - Single Student Data
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # return render(request, 'student_detail.html', {'student_data': serializer.data})
    return JsonResponse(serializer.data)

# Model object - All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return render(request, 'student_detail.html', {'student_data': serializer.data})
