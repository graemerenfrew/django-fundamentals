from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

GAME_STATUS_CHOICES = {
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'),
}
BOARD_SIZE = 3

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

    def board(self):
        ''' return a 2d list of Move objects so we can find the state of a square at y,x '''
        board=[[ None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.y][move.x] = move
        return board

    def is_users_move(self, user):
        return (user == self.first_player and self.status == 'F') or\
                (user == self.second_player and self.status =='S')

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

    def get_absolute_url(self):
        ''' this tells django what the canonical URL is for a model instance.  reverse constructs a url for us'''
        return reverse('gameplay_detail', args=[self.id])

    def new_move(self):
        ''' returns a new move object'''
        if self.status not in 'FS':
            raise ValueError("Cannot make a move as this game is over!")
        return Move(
            game=self,
            by_first_player=self.status == 'F'
        )


class Move(models.Model):
    #lets make sure the moves we enter are valid
    x = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE-1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE-1)])
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, editable=False,
                             on_delete=models.CASCADE)
    by_first_player = models.BooleanField(editable=False)

