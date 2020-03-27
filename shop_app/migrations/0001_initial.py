# Generated by Django 3.0.4 on 2020-03-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
            options={
                'verbose_name_plural': 'items',
            },
        ),
    ]
