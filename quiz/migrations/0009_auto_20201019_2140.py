# Generated by Django 3.1.2 on 2020-10-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20201019_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='status',
            field=models.CharField(choices=[('Active', '1'), ('InActive', '0')], default='0', max_length=20),
        ),
    ]
