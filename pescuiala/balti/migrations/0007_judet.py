# Generated by Django 3.2.8 on 2021-10-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balti', '0006_balta_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Judete',
            },
        ),
    ]
