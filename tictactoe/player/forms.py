from django.forms import ModelForm
# this class lets us create forms directly from models :)

from .models import Invitation

class InvitationForm(ModelForm):
    class Meta:
        '''meta classes let us configure the internal behavious of classes'''
        model = Invitation
        exclude = ('from_user', 'timestamp')