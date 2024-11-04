from django.shortcuts import render, redirect
from students.forms import StudentForm
from students.models import Student


# Create your views here.

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_students_url")
    html_file = "students/create_student.html"
    context = {"form": form}
    return render(request, html_file, context)

def show_students(request):
    students = Student.objects.all()
    context = {"students": students}
    template_file = "students/show_students.html"
    return render(request, template_file, context)

def update_student(request, s_id):
    student = Student.objects.get(id=s_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("show_students_url")
    template_name = "students/update_student.html"
    context = {"form": form}
    return render(request, template_name, context)

def delete_student(request, s_id):
    student = Student.objects.get(id=s_id)
    student.delete()
    return redirect("show_students_url")

def show_details(request, s_id):
    student = Student.objects.get(id=s_id)
    context = {"student": student}
    template_file = "students/show_details.html"
    return render(request, template_file, context)

# pip install crispy-bootstrap5
# pip install django-crispy-forms
