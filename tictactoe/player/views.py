from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    '''

        Lets delegate the creation of the html to the template using the render function
        Get the list of games that this current player is involved in

    '''
    '''
    games_first_player = Game.objects.filter(
        first_player=request.user,
        status='F'
    )
    games_second_player = Game.objects.filter(
        second_player=request.user,
        status='S'
    )
    all_my_games = list(games_first_player) + \
                    list(games_second_player)
    '''
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})