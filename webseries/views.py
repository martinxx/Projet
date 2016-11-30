from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Account,Serie,Season, Episode
from projetAPI import *
# Create your views here.

def index(request):
    account_list = Account.objects.all
    context = {'account_list': account_list}
    return render(request, 'webseries/index.html', context)

def listSerie(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'webseries/listSerie.html', {'account': account})


def listSaison(request,account_id, serie_id):
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	saisons_creees = Season.objects.all().filter(serie = serie)
	l = []
	thename = serie.name()
	for i in range(NbdeSaison(serie.serie_identifiant)):
		found = False
		for existing_season in saisons_creees : 
			if existing_season.season_text == (thename +" Saison "+str(i+1)):
				l.append(existing_season)
				found = True
		if not found : 		
			l.append(serie.season_set.create(season_text = thename+" Saison "+str(i+1), season_number = i+1))
	return render(request, 'webseries/listSaison.html', {'serie': serie, 'account' : account})

def ajoutCompte(request,nomdutexte='lol'):
	nomdutexte = request.POST['username']
	compte_ajoute = Account.objects.create(account_text =nomdutexte)
	context = {'compte_ajoute': compte_ajoute}
	return render(request, 'webseries/ajoutCompte.html', context)
	

def ajoutSerie(request,account_id,user_input='How I Met'):
	user_input = request.POST['serie_name']
	json = recherche(user_input)
	possibleseries = []
	for onepossibleserie in json["results"]:
		possibleseries.append(([ onepossibleserie["id"] ],onepossibleserie["original_name"]))
	account = get_object_or_404(Account, pk=account_id)
	return render(request, 'webseries/SelectionSerie.html', {'seriesdic': possibleseries , 'serie_name': user_input})
	
def SelectionSerie(request, account_id ):
	account = get_object_or_404(Account, pk=account_id)
	"""numserie = account.choice_set.get(pk=request.POST['choice'])"""
	numseriebrut = request.POST['nameserie']
	numserie = int(numseriebrut[1:(len(numseriebrut)-1)])
	serie_ajoutee = account.serie_set.create(serie_identifiant = numserie)
	#Toujours retourner un HttpResponseRedirect si รงa marche bien avec POST data(pour ne pas permettre de poster deux fois)
	return render(request, 'webseries/ajoutSerie.html', {'serie_ajoutee': serie_ajoutee})

def listEpisode(request,account_id, serie_id,season_id):
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	season = get_object_or_404(Season,pk=season_id)
	episode_creees = Episode.objects.filter(season = season)
	print(episode_creees)
	l = []
	#thename = season.seasonName() 		
	for i in range(NbdEpisodes(serie.serie_identifiant,season.season_number)):
		found = False
		for existing_episod in episode_creees : 
			if existing_episod.episode_text == (" Episode "+str(i+1)):
				l.append(existing_episod)
				found = True
		if not found :
			l.append(season.episode_set.create(episode_text = " Episode "+str(i+1), episode_number = i+1))
	return render(request, 'webseries/listEpisode.html', {'serie': serie, 'account' : account, 'season':season})

def episod(request,account_id, serie_id,season_id, episode_id):
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	season = get_object_or_404(Season,pk=season_id)
	episode = get_object_or_404(Episode,pk=episode_id)
	return render(request, 'webseries/Episode.html', {'serie': serie, 'account' : account, 'season': season, 'episode': episode})
