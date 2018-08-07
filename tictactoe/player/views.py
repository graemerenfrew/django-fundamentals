from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .forms import InvitationForm
from .models import Invitation
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

    #get the invitations this currently logged in user has received
    invitations = request.user.invitations_received.all()

    return render(request, "player/home.html",
                  {'games': active_games, 'invitations': invitations})


@login_required
def new_invitation(request):

    if request.method=="POST":
        invitation = Invitation(from_user=request.user) #create an object with our user id in it
        #Validate the form
        #we can now add the data the user entered into the form request together with the data in invitation, and save that
        form = InvitationForm(instance=invitation, data=request.POST) #request.POST contains whatever the user typed in
        if form.is_valid():
            form.save() #this will create a model instance and save it to the invitation table
            return redirect("player_home")
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation.html", {'form':form})

@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied

    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user
            )
        invitation.delete()
        #return redirect('player_home')
        return redirect(game) #this will call get_absolute_url for the game object
    else:
        return render(request,
                      "player/accept_invitation_form.html",
                      {'invitation':invitation})