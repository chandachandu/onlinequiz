# Generated by Django 3.1.2 on 2020-10-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_useranswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswers',
            name='q1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q10',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q7',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q8',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='q9',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswers',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]