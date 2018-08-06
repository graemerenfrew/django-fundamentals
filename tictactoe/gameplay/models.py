from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="games_first_player")
    second_player = models.ForeignKey(User,
                                      related_name="games_second_player")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)


class Move(models.Model):
    ''' this is a model class and will rep a table in the database
        PrimaryKey will be added automatically
    '''
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)


