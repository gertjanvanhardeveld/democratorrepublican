from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party


def homepage(request):
    greeting = "Political preference"
    parties = Party.objects.all()
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
