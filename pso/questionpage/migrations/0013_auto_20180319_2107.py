# Generated by Django 2.0.2 on 2018-03-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpage', '0012_auto_20180319_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
