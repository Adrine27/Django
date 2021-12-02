# Generated by Django 3.2.9 on 2021-11-24 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('photo', models.ImageField(upload_to='class', verbose_name='Photo')),
                ('address', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('license', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Cigarette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('slug', models.SlugField(unique=True)),
                ('photo', models.ImageField(upload_to='class', verbose_name='Photo')),
                ('count', models.PositiveIntegerField(verbose_name='count')),
                ('date', models.DateField()),
                ('nicotine', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('xej', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('choices', models.CharField(choices=[('thin', 'Thin'), ('thick', 'Thick')], default='Thick', max_length=6)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
            ],
        ),
    ]
