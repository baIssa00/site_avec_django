# Generated by Django 4.0.4 on 2022-06-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='link',
            field=models.ImageField(upload_to='images'),
        ),
    ]
