# Generated by Django 2.0.1 on 2018-02-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20180210_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='PostStorage'),
        ),
    ]
