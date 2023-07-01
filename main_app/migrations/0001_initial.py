# Generated by Django 4.2.2 on 2023-07-01 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shade_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rgb', models.CharField(max_length=15)),
                ('hex', models.CharField(max_length=50)),
                ('base_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shade', to='main_app.base_color')),
            ],
        ),
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('colors', models.ManyToManyField(to='main_app.shade_color')),
            ],
        ),
    ]
