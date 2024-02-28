# Generated by Django 3.2.12 on 2024-02-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelapp', '0003_parents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=20)),
                ('Author', models.CharField(max_length=20)),
                ('Created_at', models.DateTimeField()),
            ],
        ),
    ]
