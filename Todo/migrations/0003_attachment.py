# Generated by Django 3.2.6 on 2021-09-05 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_auto_20210828_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=125)),
                ('file', models.FileField(max_length=500, upload_to='attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('attached_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity', to='Todo.todo')),
            ],
        ),
    ]