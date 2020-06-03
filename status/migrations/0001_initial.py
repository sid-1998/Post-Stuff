# Generated by Django 2.2.1 on 2020-06-03 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import status.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=10000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_image)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
