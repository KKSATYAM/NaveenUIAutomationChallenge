# Generated by Django 5.0.6 on 2024-06-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eno", models.IntegerField()),
                ("ename", models.CharField(max_length=64)),
                ("esal", models.IntegerField()),
                ("eaddr", models.CharField(max_length=64)),
            ],
        ),
    ]