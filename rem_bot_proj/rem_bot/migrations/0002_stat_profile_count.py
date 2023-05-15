# Generated by Django 4.2.1 on 2023-05-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rem_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.PositiveIntegerField(unique=True, verbose_name='Дата')),
                ('count', models.TextField(verbose_name='Кол-во')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистик',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='count',
            field=models.TextField(default=0, verbose_name='Количество запросов'),
            preserve_default=False,
        ),
    ]