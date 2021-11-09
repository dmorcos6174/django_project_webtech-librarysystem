# Generated by Django 3.2.5 on 2021-07-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrow_to',
        ),
        migrations.AddField(
            model_name='book',
            name='borrow_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='return_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
