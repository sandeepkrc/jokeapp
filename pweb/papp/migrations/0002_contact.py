# Generated by Django 3.0.4 on 2020-03-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=96)),
                ('message', models.TextField()),
            ],
        ),
    ]
