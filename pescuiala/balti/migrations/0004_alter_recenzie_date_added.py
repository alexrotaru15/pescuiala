# Generated by Django 3.2.8 on 2021-10-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balti', '0003_auto_20211020_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recenzie',
            name='date_added',
            field=models.DateTimeField(verbose_name='Data adaugare'),
        ),
    ]
