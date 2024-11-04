import os
from uuid import uuid4

from django.db import models

def generate_unique_name(instance, filename):
    name  = uuid4()
    ext = filename.split('.')[-1]
    full_file_name = f'{name}.{ext}'
    return os.path.join('students', full_file_name)

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    dob = models.DateField()
    completed = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=generate_unique_name,null=True, default="students/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # pip install Pillow