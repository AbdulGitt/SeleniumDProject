# Generated by Django 5.0.2 on 2024-02-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyEmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('name', models.CharField(max_length=16)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee_Details',
        ),
        migrations.DeleteModel(
            name='EmployeeModel',
        ),
    ]