
from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    name = models.TextField(max_length=255)
    def __str__(self):
        return f'{self.id} {self.name}'

class Student(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    address = models.TextField()
    age = models.IntegerField(default=20)
    email = models.EmailField(blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return f'MSSV: {self.id}, Ten: {self.name}, Dia chi: {self.address}, Tuoi: {self.age}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
    

class Course(models.Model):
    name = models.TextField(max_length=255)
    limit = models.IntegerField(default=30)
    startdate = models.DateField()
    enddate = models.DateField()
    student = models.ManyToManyField(Student, blank=True, null= True)

    def __str__(self):
        return f'{self.name} ({self.id})'