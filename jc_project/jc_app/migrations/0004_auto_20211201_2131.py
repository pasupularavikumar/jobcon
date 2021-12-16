# Generated by Django 3.2.9 on 2021-12-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc_app', '0003_jobform_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics/%y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('action_name', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('sub_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='slide',
        ),
    ]
