# Generated by Django 2.2.5 on 2020-04-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0006_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
