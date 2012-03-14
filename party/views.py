from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party


def homepage(request):
    greeting = "What's your political preference?"
    parties = Party.objects.all()
    return render_to_response('homepage.html', {
        'parties': parties,
        'greeting': greeting,
    })

