# Generated by Django 3.1.7 on 2021-03-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210322_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name_plural': 'artists'},
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default=True, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
