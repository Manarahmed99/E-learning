# Generated by Django 4.2.10 on 2024-03-11 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_product', models.IntegerField()),
                ('Id_user', models.IntegerField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('total', models.FloatField()),
                ('discount', models.FloatField()),
                ('net', models.FloatField()),
                ('status', models.BooleanField()),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('itemsid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TechEdu.items')),
            ],
        ),
    ]