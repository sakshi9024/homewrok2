from django.shortcuts import render,HttpResponse
from .models import Student
from .forms import StudentForm


def index(request):
    if request.method=="POST":
        form_data= StudentForm(request.post,request.files)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse("data saved")
        form_data = StudentForm()
        data = Student.objects.all()
        context = {
            'form_data':form_data,
            'data':data
        }
        return render(request,'index.html',context)

