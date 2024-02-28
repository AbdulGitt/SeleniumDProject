from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MyEmployeeForm
from .models import MyEmployeeData


# Create your views here.
def retrieveemployeedata(request):
    employee=MyEmployeeData.objects.all()
    data=serializers.serialize('json',employee)
    # return HttpResponse(data,content_type='application/json')
    return render(request,"RegisterPage//employeedetails.html",context={"employee":employee})

def showemployeedata(request):
    employee=MyEmployeeData.objects.all()
    data=serializers.serialize('json',employee)
    # return HttpResponse(data,content_type='application/json')
    return render(request,"RegisterPage//employeedetails.html",context={"employee":employee})

def addemployeedata(request):
    if request.method=="POST":
        form=MyEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Successfully stored data in Database")
            return redirect("/employeedetails/")
        else:
            return HttpResponse("Some fields are missing")
    form=MyEmployeeForm()
    return render(request,"RegisterPage//addemployee.html",context={"form":form})


def deleteemployee(request,id):
    employee=MyEmployeeData.objects.get(id=id)
    employee.delete()
    return HttpResponse("<h2>Succesfully deleted the data in DB<a href='/employeedetails/'>Click Here</a> to Employee Database</h2>")


def updateemployee(request,id):
    employee = MyEmployeeData.objects.get(id=id)
    if request.method=="POST":
        form=MyEmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Successfully updated the data in DB<a href='/employeedetails/'>Click Here</a> to Employee Database</h2>")
        else:
            return HttpResponse("Some fields are missing")
    return render(request,"RegisterPage//updateemployee.html",context={"employee":employee})

