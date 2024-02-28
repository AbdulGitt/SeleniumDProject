from django.db import models

class MyEmployeeData(models.Model):
    employee_id=models.IntegerField()
    name=models.CharField(max_length=16)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name
