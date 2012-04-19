from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response 
from democratorrepublican.party.models import Party, CustomUserForm, CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect

def homepage(request):
    if request.user.is_authenticated():
        try:
            picked = CustomUser.objects.get(user__username=request.user)
        except:
            picked = []
        if picked:
           parties = Party.objects.order_by('party')
           greeting = "Welcome. Pick a party please"
           form = []
        else:
            if request.method == 'POST': # If the form has been submitted...
                parties =[]
                greeting = "Welcome. Pick a party please"
                form = CustomUserForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                    #form.user = request.user.id
                    form.save()
                    return HttpResponseRedirect('/maps/') # Redirect after POST
            else:
                parties = []
                greeting = "Welcome. Pick a party please"
                form = CustomUserForm() # An unbound form
    else:
        greeting = "You are not logged in. Log in to share your Political Preference." 
        form = []
        parties = []  
    return render_to_response('homepage.html', {
        'form': form,
        'greeting': greeting,
        'parties': parties,
    }, context_instance=RequestContext(request))

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

def republicans(request):
    return render_to_response('republicans.html', {
    })

def otherparties(request):
    return render_to_response('otherparties.html', {
    })

def detail(request, party_id):
    greeting = "Thanks for your support! Your political preference is:"
    party = Party.objects.get(id=party_id)
    people = CustomUser.objects.filter(party=party)
    return render_to_response('detail.html', {
        'party': party,
        'greeting': greeting,
        'people': people,
    })

@csrf_protect
def create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserCreationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/accounts/login/') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form
    return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))



