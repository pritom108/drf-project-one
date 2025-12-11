from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student



def studentView(request):


    """
    students= {
        'id': 1,
        'name': 'Pritom karmoker',
        'class': 'computer Science'

    }
    return JsonResponse(students)

    """



    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
