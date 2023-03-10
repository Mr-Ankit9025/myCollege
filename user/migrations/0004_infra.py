# Generated by Django 3.2.4 on 2022-09-09 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_mycourse_hodpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='infra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('stupic', models.ImageField(null=True, upload_to='static/profile')),
                ('designation', models.CharField(max_length=70)),
                ('syear', models.CharField(max_length=40)),
                ('cpic', models.ImageField(upload_to='static/company')),
                ('rdate', models.DateField()),
                ('pcity', models.CharField(max_length=60)),
                ('cname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.company')),
            ],
        ),
    ]
