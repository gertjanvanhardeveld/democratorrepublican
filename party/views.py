from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party


def homepage(request):
    greeting = "What's your political preference?"
    parties = Party.objects.all()
    return render_to_response('homepage.html', {
        'parties': parties,
        'greeting': greeting,
    })




def detail(request, party_id):
    party = Party.objects.get(id=party_id)
    return render_to_response('detail.html', {
        'party': party,
    })
