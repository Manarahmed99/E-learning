# Generated by Django 4.2.10 on 2024-03-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechEdu', '0003_remove_cart_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='title',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
