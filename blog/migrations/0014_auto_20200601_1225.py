# Generated by Django 3.0.6 on 2020-06-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200601_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.TextField(default='hey guys leave your comments', max_length=1160),
        ),
    ]
