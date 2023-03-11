from django.shortcuts import render

# Create your views here.
def html_project(request):
    return render(request,'html_project.html')
