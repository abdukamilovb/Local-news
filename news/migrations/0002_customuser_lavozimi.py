# Generated by Django 5.1.6 on 2025-03-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lavozimi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
