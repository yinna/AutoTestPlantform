# Generated by Django 3.1.3 on 2021-01-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0005_db_apis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_apis',
            name='body_method',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
