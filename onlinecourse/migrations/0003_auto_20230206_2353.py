# Generated by Django 3.1.3 on 2023-02-06 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230206_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='questions',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
    ]
