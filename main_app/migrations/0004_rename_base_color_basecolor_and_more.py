# Generated by Django 4.2.2 on 2023-07-01 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_shade_color_base_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base_color',
            new_name='BaseColor',
        ),
        migrations.RenameModel(
            old_name='Shade_color',
            new_name='ShadeColor',
        ),
    ]
