# Generated by Django 3.2.9 on 2021-11-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name="Flower's name")),
                ('price', models.PositiveIntegerField(default=1000)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('count', models.PositiveSmallIntegerField(default=1)),
                ('color', models.CharField(choices=[('red', 'Red'), ('white', 'White')], max_length=5)),
            ],
            options={
                'verbose_name': 'Flower',
                'verbose_name_plural': 'Flowers',
            },
        ),
    ]
