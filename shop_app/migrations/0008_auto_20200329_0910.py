# Generated by Django 3.0.4 on 2020-03-29 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_auto_20200329_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='thumbnail',
            field=models.ImageField(blank=True, default='profile_default.jpg', upload_to='pics'),
        ),
    ]
