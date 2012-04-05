from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party

from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    if request.user.is_authenticated():
        greeting = "You are logged in. Yay!"
        parties = Party.objects.filter(customuser=request.user)
    else:
        greeting = "You are not logged in. Fail!" 
        parties = []
    return render_to_response('homepage.html', {
        'parties': parties,
        'greeting': greeting,
    })




def detail(request, party_id):
    greeting = "Thanks! Your political preference is:"
    party = Party.objects.get(id=party_id)
    return render_to_response('detail.html', {
        'party': party,
        'greeting': greeting,
    })
