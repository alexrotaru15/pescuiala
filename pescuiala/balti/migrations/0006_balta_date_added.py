# Generated by Django 3.2.8 on 2021-10-20 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('balti', '0005_alter_recenzie_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='balta',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data adaugare'),
            preserve_default=False,
        ),
    ]