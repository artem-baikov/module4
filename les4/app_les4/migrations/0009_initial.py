# Generated by Django 4.0.10 on 2023-08-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_les4', '0008_delete_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('auction', models.BooleanField(help_text='отметьте, если торг возможен', verbose_name='торг')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')),
            ],
            options={
                'db_table': 'advertisements',
            },
        ),
    ]
