# Generated by Django 2.0b1 on 2019-12-11 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191211_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='addressedTo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
