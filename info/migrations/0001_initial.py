# Generated by Django 2.2 on 2022-01-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
            ],
        ),
    ]
