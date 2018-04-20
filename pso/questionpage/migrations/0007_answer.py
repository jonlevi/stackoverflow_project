# Generated by Django 2.0.2 on 2018-02-20 02:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionpage', '0006_auto_20180219_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_answered', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='questionpage.Question')),
            ],
        ),
    ]
