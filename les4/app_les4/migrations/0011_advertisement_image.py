# Generated by Django 4.0.10 on 2023-08-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_les4', '0010_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]