# Generated by Django 3.1.2 on 2021-12-01 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211201_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Имя', max_length=50, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='group_number',
            field=models.CharField(help_text='Номер группы', max_length=30, verbose_name='group_number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Фамилия', max_length=50, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronym',
            field=models.CharField(help_text='Отчество (при отсутствии отметьте символом "-")', max_length=50, verbose_name='patronym'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Юзернейм', max_length=50, unique=True, verbose_name='username'),
        ),
    ]
