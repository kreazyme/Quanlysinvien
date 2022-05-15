
from ast import keyword
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from matplotlib.style import context
from .forms import StudentForm
from .models import Student


def index(request):
    response = HttpResponse()
    response.writelines('<h1>This is homepage</h1>')
    response.write('Home page is here')
    return response

def testhtml(request):
    context = {
        "name": "Tran Duc Thong",
        "skill": "Xin chao"
    }
    return render(request, 'home.html', {"name": "Tran Duc Thong", "skills": ["Xin chao", "Tran Duc"], "data": [1,2,3,4,5,6]})

def detailview(request, id):
    std = get_object_or_404(Student, id = id)
    return render(request, "detail.html", {"students": std})

# def viewcreate(request):
#     form = StudentForm()
#     return render(request, 'create.html', {'form': form})

def viewcreate(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
        return redirect('/list')
    return render(request, 'create.html', {'form': form})

def viewdelete(request, id):
    student = get_object_or_404(Student, id = id)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST':
        student.delete()
        return redirect('/list')
    context = {
        'student': student
    }
    return render(request, 'delete.html', context)

def viewupdate(request, id):
    std = get_object_or_404(Student, id = id)
    form = StudentForm(request.POST or None, instance=std)

    if request.method == "POST":
        form.save()
        return redirect('/list')

    context = {'form' : form}
    return render(request, "update.html", context)

def viewlist(request):
    keyword = request.GET.get('keyword')

    if keyword:
        stds = Student.objects.filter(code__icontains = keyword)
    else:
        stds = Student.objects.all()

    context = {
        'keyword' : keyword,
        'students': stds.order_by('code')
    }
    return render(request, 'listview.html', context)
