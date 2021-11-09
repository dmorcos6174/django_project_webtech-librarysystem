# Generated by Django 3.2.5 on 2021-07-19 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_author', models.CharField(default='Unknown', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('isbn', models.CharField(max_length=5, unique=True)),
                ('borrowed', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('borrow_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Borrowed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]