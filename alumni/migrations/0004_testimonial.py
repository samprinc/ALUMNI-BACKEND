# Generated by Django 5.2.2 on 2025-07-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0003_librarydocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
