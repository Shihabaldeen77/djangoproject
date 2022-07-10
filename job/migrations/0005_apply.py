# Generated by Django 3.2.14 on 2022-07-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20220706_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('vewsite', models.URLField()),
                ('cv', models.FileField(upload_to='Apply/')),
                ('couver_letter', models.TextField(max_length=500)),
            ],
        ),
    ]
