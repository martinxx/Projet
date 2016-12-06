import datetime
from django.db import models
from django.utils import timezone
from projetAPI import * 

"""Ce fichier comptient l'ensemble de nos classes"""

class Account(models.Model):
	"""Cette classe représente un compte utilisateur"""
	account_text = models.CharField(max_length=200)

	def __str__(self):
		return self.account_text

class Serie(models.Model):
	"""Cette classe représente une série. Elle est nécessairement liée à un compte : 
	Si Martin et Charles regardent "The Simpsons", il y aura deux instances de classe série concernant "The Simpsons":
	Une liée au compte de Martin, l'autre liée au compte de Charles."""
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	serie_identifiant = models.IntegerField(default = 0)
	
	"""Les méthodes renvoient nom, photo, descriptif de la série et autres informations"""
	
	def name(self):
		return nom(self.serie_identifiant)

	def __str__(self):
		return str(self.serie_identifiant)

	def photo(self):
		return photo(self.serie_identifiant)

	def overview(self):
		res = JSserie(self.serie_identifiant)["overview"]
		if res =="":
			return "Sorry, no overview was available in our database"
		else : 
			return res

	def listSaison(self):
		"Renvoit la liste des Saisons (comme des chaînes de caractères, pas des objets saison) de la série"
		nbSaison = NbdeSaison(self.serie_identifiant)
		l=[]
		for i in range(nbSaison):
			l.append("Saison "+ str(i+1))
		return l
		
	def NouveauEpisode(self):
			return NextEpisode(self.serie_identifiant)

	def hasNouveauEpisode(self):
		return hasNextEpisode(self.serie_identifiant)

	def creator(self):
		a = JSserie(self.serie_identifiant)["created_by"]
		res = []
		for i in range(len(a)):
			res.append(a[i]["name"])
		if len(res) ==0:
			return "Sorry, no creator was in our database"
		else :
			return ", ".join(res)

class Season(models.Model):
	"""Cette classe représente une saison (avec son numéro de saison notamment).
	Elle est liée à une instance de classe Série en particulier"""
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
	season_text = models.CharField(max_length=200,default ="Noname")
	season_number = models.IntegerField(default = 0)
	
	"""Les méthodes sont sensiblement les mêmes une pour une série"""

	def seasonName(self):
		return nomSaison(self.serie.serie_identifiant, self.season_number)

	def __str__(self):
		return self.season_text+str(self.season_number)

	def photo2(self):
		 return photoSaison(self.serie.serie_identifiant,self.season_number)

 
	def overview2(self):
		res = JSSaison(self.serie.serie_identifiant,self.season_number)["overview"]
		if res =="":
			return "Sorry, no overview was available in our database"
		else :
			return res

	def listEpisode(self):
		"""Renvoit la liste des épisodes (sous forme de chaîne de caractère, pas les instances de classe Episode) de la saison"""
		nbEpisode = NbdEpisodes(self.serie.serie_identifiant,self.season_number)
		l=[]
		for i in range(nbEpisode):
			l.append("Episode "+ str(i+1))
		return l

class Episode(models.Model):
	"""Cette classe représente un épisode (avec son numéro de saison notamment).
	Elle est liée à une instance de classe Saison en particulier"""
	season = models.ForeignKey(Season, on_delete=models.CASCADE)
	episode_text = models.CharField(max_length=200,default= "Noname")
	episode_number = models.IntegerField(default = 0)

	def episodeName(self):
		return "Season " + str(self.season.season_number)+" Episode " +str(self.episode_number)

	def __str__(self):
		return self.episode_text+str(self.episode_number)

	def episodeName2(self):
		return JSEpisode(self.season.serie.serie_identifiant, self.season.season_number, self.episode_number)["name"]
	
	def overview_episode(self):
		res = JSEpisode(self.season.serie.serie_identifiant,self.season.season_number, self.episode_number)["overview"]
		if res =="":
			return "Sorry, no overview was available in our database"
		else : 
			return res

	def photo_episode(self):
         return photoEpisode(self.season.serie.serie_identifiant,self.season.season_number, self.episode_number)

	def __str__(self):
		return self.episode_text+str(self.episode_number)




