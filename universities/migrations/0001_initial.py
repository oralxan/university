# Generated by Django 4.2.8 on 2024-02-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name univer')),
                ('address', models.TextField(verbose_name='address')),
                ('phone_number', models.CharField(max_length=13, verbose_name='uni num')),
                ('image', models.ImageField(upload_to='university-image/', verbose_name='img univer')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universitys',
            },
        ),
    ]