from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party

from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    if request.user.is_authenticated():
        greeting = "You are logged in!"
        parties = Party.objects.all()
    else:
        greeting = "You are not logged in. Log in to share your Political Preference." 
        parties = []
    return render_to_response('homepage.html', {
        'parties': parties,
        'greeting': greeting,
    })




def detail(request, party_id):
    greeting = "Thanks for your support! Your political preference is:"
    party = Party.objects.get(id=party_id)
    return render_to_response('detail.html', {
        'party': party,
        'greeting': greeting,
    })
