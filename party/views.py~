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

def about(request):
    greeting = "Welcome on Political Preference"
    return render_to_response('about.html', {
        'greeting': greeting,
    })

def maps(request):
    greeting = "Explore the world of Political Preferences"
    return render_to_response('maps.html', {
        'greeting': greeting,
    })

def democrats(request):
    return render_to_response('democrats.html', {
    })

def detail(request, party_id):
    greeting = "Thanks for your support! Your political preference is:"
    party = Party.objects.get(id=party_id)
    return render_to_response('detail.html', {
        'party': party,
        'greeting': greeting,
    })
