# Generated by Django 2.1 on 2018-08-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_auto_20180807_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('D', 'Draw'), ('W', 'First Player Wins'), ('F', 'First Player to Move'), ('S', 'Second Player to Move'), ('L', 'Second Player Wins')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(editable=False),
        ),
    ]
