import json
import urllib.request
import smtplib
from datetime import date
from django.db import models

key = "5c3fde1ab28b3cb007c61d944b4d4c94" 
"""cette clé gratuite pour accéder à l'api themoviedb nous autorise à 1000 requêtes par jour """ 

def recherche(nomvoulu, key = key):
    """Renvoie un JSON qui correspond à l'ensemble des séries ayant un nom proche de l'entrée """
    nom = urllib.parse.quote(nomvoulu)
    urllink = 'https://api.themoviedb.org/3/search/tv?api_key='+key+'&query='+nom
    data = urllib.request.urlopen(urllink).read()
    js = json.loads(data.decode())
    return js 

def JSserie(idSerie):
    """Renvoie le JSON correspondant à la serie"""
    urlserie = "https://api.themoviedb.org/3/tv/"+ str(idSerie) + "?api_key=" + key
    data = urllib.request.urlopen(urlserie).read()
    js = json.loads(data.decode())
    return(js)

def nom(idSerie, key = key):
    """Renvoie le nom de la série"""
    js = JSserie(idSerie)
    resultat = js["original_name"] 
    return resultat

def photo(idSerie, key = key):
    """Renvoie un lien html avec la photo de la série au format jpg"""
    js = JSserie(idSerie)
    path = js["poster_path"]
    urllink = "https://image.tmdb.org/t/p/w500/"+str(path) 
    return urllink

def NbdeSaison(idSerie):
    """Renvoie un entier correspondant aux nombres de saisons de la série"""
    js = JSserie(idSerie)
    return(int(js["number_of_seasons"]))

def nomSaison(idSerie, idSaison):
    """Renvoie le nom de la saison"""
    js = JSSaison(idSerie, idSaison)
    resultat = js["name"] 
    return resultat

def photoSaison(idSerie, numSaison):
    """Renvoie un lien html avec la photo de la saison au format jpg"""
    js = JSSaison(idSerie, numSaison)
    path = js["poster_path"]
    urllink = "https://image.tmdb.org/t/p/w500/"+str(path) 
    return urllink

def NbdEpisodes(idSerie, numSaison):
    """Renvoie un entier correspondant aux nombres d'épisodes de la saison de la série"""
    js = JSserie(idSerie)
    res = js["seasons"]["season_number"==numSaison]["episode_count"]
    return res
    # return(int(js["episode_count"]))
    
def JSSaison(idSerie,numSaison, key = key):
    """Renvoie un JSON qui donne l'ensemble des épisodes de cette saison pour cette série"""
    urllink = "https://api.themoviedb.org/3/tv/"+str(idSerie)+"/season/"+str(numSaison)+ "?api_key="+key
    data = urllib.request.urlopen(urllink).read()
    js = json.loads(data.decode())
    return js 

def JSEpisode(idSerie,numSaison, idEpisode, key = key):
    """Renvoie un JSON qui donne l'épisode de cette saison pour cette série"""
    urllink = "https://api.themoviedb.org/3/tv/"+str(idSerie)+"/season/"+str(numSaison)+"/episode/"+str(idEpisode)+"?api_key="+key
    data = urllib.request.urlopen(urllink).read()
    js = json.loads(data.decode())
    return js 

def nameEpisode(idSerie, idSaison, idEpisode):
	"""Renvoie le nom de l episode"""
	js = JSEpisode(idSerie, idSaison,idEpisode)
	resultat = js["name"] 
	return resultat

def isnew(airdate):     
	"""Renvoie un booleen : Vrai si airdate > today. Airdate est de la forme 'YYYY-MM-DD' """
	"""Cette fonction sert à tester si un épisode a déjà été diffusé ou pas"""
	l = airdate.split("-")
	episodedate = date(int(l[0]), int(l[1]), int(l[2]))
	return episodedate >= date.today()

def compare (date1,date2):   
	"""Fonction qui compare deux dates (afin de choisir l'épisode le moins récent qui n'a pas encore été diffusé)"""
	"""Si la base de données contient deux épisodes non diffusé, on ne déclenche une alerte que sur le prochain"""
	premiereliste = date1.split("-")
	deuxiemeliste = date2.split ("-")
	episodedate1 = date(int(premiereliste[0]), int(premiereliste[1]), int(premiereliste[2]))
	episodedate2 = date(int( deuxiemeliste[0]), int( deuxiemeliste[1]), int( deuxiemeliste[2]))
	return episodedate1 > episodedate2

def NextEpisode(idSerie):
    """Retourne un dictionnaire renvoyant les informations du prochain épisode de la série s'il existe. Retourne un dictionnaire vide sinon"""
    numLastSeason = NbdeSaison(idSerie)
    lastSeason = JSSaison(idSerie,numLastSeason, key = key)
    next_episode = {"air_date" : "3000-01-01" }
    for episode in lastSeason["episodes"]:
        if (isnew(episode["air_date"]) and compare(next_episode["air_date"] , episode["air_date"])) :
            next_episode = episode
    if (next_episode["air_date"]) == "3000-01-01" :
        return "Sorry, no new episode available"
    else:
        return "Next episode: "+ next_episode["name"] + " , air date : " + next_episode["air_date"]
    

def envoiMail(destinataire,msg,expediteur = "webseriespython5@gmail.com"):
    """Envoie un mail sans objet au destinaire avec l'adresse webserie"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(expediteur, "Python123")
    server.sendmail(expediteur, destinataire, msg)
    server.quit()
