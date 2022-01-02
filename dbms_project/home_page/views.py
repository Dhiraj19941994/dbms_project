from django.shortcuts import render
from django.http import HttpResponse


# Creating our home page
def home_page(request):
    name ="Ashok"
    age = 25
    context = {'name':name,'age':age}
    return render(request,'home_page/index.html',context=context)
