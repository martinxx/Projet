from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Account,Serie,Season, Episode
from projetAPI import *
"""Ce fichier contient nos vues"""

def index(request):
	"""Notre index est constitué de la liste des comptes utilisateurs"""
	account_list = Account.objects.all
	context = {'account_list': account_list}
	return render(request, 'webseries/index.html', context)

def listSerie(request, account_id):
	"""Génère la liste des séries suivies par un compte donné"""
	account = get_object_or_404(Account, pk=account_id)
	return render(request, 'webseries/listSerie.html', {'account': account})


def listSaison(request,account_id, serie_id):
	"""Génère la liste des saisons d'une série donnée"""
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	saisons_creees = Season.objects.all().filter(serie = serie)
	l = []
	thename = serie.name()
	for i in range(NbdeSaison(serie.serie_identifiant)):
		found = False
		for existing_season in saisons_creees : 
			if existing_season.season_text == (thename +" Season "+str(i+1)):
				l.append(existing_season)
				found = True
		if not found : 		
			l.append(serie.season_set.create(season_text = thename+" Season "+str(i+1), season_number = i+1))
	return render(request, 'webseries/listSaison.html', {'serie': serie, 'account' : account})

def ajoutCompte(request,nomdutexte=''):
	"""Fonction de création d'un nouveau compte utilisateur"""
	nomdutexte = request.POST['username']
	if nomdutexte == "":
		return render(request, 'webseries/ajoutCompteechec.html')
	else:
		compte_ajoute = Account.objects.create(account_text =nomdutexte)
		context = {'compte_ajoute': compte_ajoute}
		return render(request, 'webseries/ajoutCompte.html', context)
	

def ajoutSerie(request,account_id,user_input='Dummy'):
	"""Fonction pour ajouter une nouvelle série"""
	"""La fonction va rechercher grâce à l'API la liste des séries dont le nom correspond à l'entrée de l'utilisateur"""
	user_input = request.POST['serie_name']
	if user_input == "":
		return render(request,'webseries/SelectionSerieechec.html')
	else:
		json = recherche(user_input)
		possibleseries = []
		for onepossibleserie in json["results"]:
			possibleseries.append(([ onepossibleserie["id"] ],onepossibleserie["original_name"]))
		account = get_object_or_404(Account, pk=account_id)
		if possibleseries == []:
			return render(request, 'webseries/SelectionSerieechec.html')
		else:
			return render(request, 'webseries/SelectionSerie.html', {'seriesdic': possibleseries , 'serie_name': user_input})
	
def SelectionSerie(request, account_id ):
	"""Fonction qui permet à l'utilisateur de sélectionner la série qui l'intéresse parmis les choix proposés"""
	account = get_object_or_404(Account, pk=account_id)
	numseriebrut = request.POST['nameserie']
	numserie = int(numseriebrut[1:(len(numseriebrut)-1)])
	serie_ajoutee = account.serie_set.create(serie_identifiant = numserie)
	return render(request, 'webseries/ajoutSerie.html', {'serie_ajoutee': serie_ajoutee})

def listEpisode(request,account_id, serie_id,season_id):
	"""Génère la liste des épisodes pour une saison donnée """
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	season = get_object_or_404(Season,pk=season_id)
	episode_creees = Episode.objects.filter(season = season)
	print(episode_creees)
	l = []
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
	"""Renvoit sur la page html de l'épisode demandé"""
	account = get_object_or_404(Account, pk=account_id)
	serie = get_object_or_404(Serie, pk=serie_id)
	season = get_object_or_404(Season,pk=season_id)
	episode = get_object_or_404(Episode,pk=episode_id)
	return render(request, 'webseries/Episode.html', {'serie': serie, 'account' : account, 'season': season, 'episode': episode})
