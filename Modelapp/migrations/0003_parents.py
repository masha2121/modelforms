# Generated by Django 3.2.12 on 2024-02-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelapp', '0002_auto_20240228_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullnames', models.CharField(max_length=20)),
                ('Email_address', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
            ],
        ),
    ]