# Generated by Django 4.2.7 on 2024-02-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ManyToManyField(to='restaurant_menu.menu')),
            ],
        ),
    ]
