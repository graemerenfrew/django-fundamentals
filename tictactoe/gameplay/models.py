from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

GAME_STATUS_CHOICES = {
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'),
}

class GameQuerySet(models.QuerySet):
    ''' this will represent a collection of objects from the database'''
    def games_for_user(self, user):

        #We have imported Q which lets us do queries with logical OR in them
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        ''' return active games'''
        return self.filter(
            Q(status='F') | Q(status='S')
        )

@python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name="games_first_player",
                                     on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,
                                      related_name="games_second_player",
                                      on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)


    #Create an overwritten manager object that will contain the objects from the GamesQuerySet custom object
    objects = GameQuerySet.as_manager()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE)
