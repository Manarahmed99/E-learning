# Generated by Django 4.2.10 on 2024-03-11 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechEdu', '0002_remove_itemdetails_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='qty',
        ),
    ]