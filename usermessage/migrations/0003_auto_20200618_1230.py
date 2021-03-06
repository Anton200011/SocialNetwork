# Generated by Django 3.0.3 on 2020-06-18 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermessage', '0002_auto_20200618_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialog',
            name='participant1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='participant1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dialog',
            name='participant2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='participant2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
