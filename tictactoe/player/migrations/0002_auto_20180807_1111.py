# Generated by Django 2.1 on 2018-08-07 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True, help_text='Always nice to be friendly!', max_length=300, verbose_name='Optional message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text='Please select the user you wnat to challenge!', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]
