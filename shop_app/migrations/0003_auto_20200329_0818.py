# Generated by Django 3.0.4 on 2020-03-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='thumbnail',
            field=models.ImageField(default='profile_default.jpg', upload_to='pics'),
        ),
    ]