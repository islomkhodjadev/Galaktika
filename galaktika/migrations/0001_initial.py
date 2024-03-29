# Generated by Django 5.0.1 on 2024-01-16 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome', models.CharField(max_length=50, verbose_name='xush kelibsiz')),
                ('content', models.TextField(max_length=500, verbose_name='haqida')),
            ],
            options={
                'verbose_name': 'Haqida',
                'verbose_name_plural': 'Haqida',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage', models.CharField(max_length=200, verbose_name='ustunlik')),
                ('content', models.CharField(max_length=200, verbose_name='qanday')),
            ],
            options={
                'verbose_name': 'ustunlik',
                'verbose_name_plural': 'qanday',
            },
        ),
        migrations.CreateModel(
            name='CategoryContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fillial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Learners_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Turkumi')),
                ('count', models.IntegerField(verbose_name='Soni')),
            ],
            options={
                'verbose_name': 'Statistika',
                'verbose_name_plural': 'Statistika',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kurs ismi')),
                ('about', models.TextField(max_length=400, verbose_name='Haqida')),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='index/courses/img', verbose_name='rasm')),
                ('img_webp', models.ImageField(blank=True, upload_to='index/courses/img_webp')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaktika.categorycourse')),
            ],
            options={
                'verbose_name': 'Kurslar',
                'verbose_name_plural': 'Kurslar',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='sarlavha')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField(max_length=500, verbose_name='maqola')),
                ('image', models.ImageField(upload_to='index/events/img', verbose_name='rasm')),
                ('img_webp', models.ImageField(blank=True, upload_to='index/events/img_webp')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaktika.categorycontent', verbose_name='turi')),
                ('fillial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaktika.fillial', verbose_name='fillial')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=400, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=400, null=True)),
                ('telegram', models.CharField(blank=True, max_length=400, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='ism')),
                ('about', models.TextField(max_length=400, verbose_name='haqida')),
                ('image', models.ImageField(upload_to='index/teachers/img', verbose_name='rasm')),
                ('img_webp', models.ImageField(blank=True, upload_to='index/teachers/img_webp')),
                ('filial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaktika.fillial')),
            ],
            options={
                'verbose_name': "O'qituvchilar",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='student ismi')),
                ('surname', models.CharField(max_length=50, verbose_name='student familiyasi')),
                ('phone', models.CharField(max_length=13, verbose_name='nomer')),
                ('active', models.BooleanField(blank=True, default=False, verbose_name="O'qimoqda")),
                ('courses', models.ManyToManyField(blank=True, to='galaktika.course', verbose_name='yozilgan kurslari')),
                ('filliallar', models.ManyToManyField(blank=True, to='galaktika.fillial', verbose_name='filliallar')),
                ('teachers', models.ManyToManyField(blank=True, to='galaktika.teacher', verbose_name="o'qituvchilari")),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Studentlar',
            },
        ),
    ]
