import datetime
from django.db import models
from django.utils import timezone
from projetAPI import * 
import json # Create your models here.

class Account(models.Model):
    account_text = models.CharField(max_length=200)

    def __str__(self):
        return self.account_text
    # def Ajout_compte(self,nomCompte):
    #     Account.objects.create(account_text =nomCompte)
    #     return nomCompte



class Serie(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    serie_identifiant = models.IntegerField(default = 0)
    serie_json = models.CharField(max_length=200000,default ="{}")
    #a = str(serie_identifiant)
    #serie_photo = JSserie(serie_identifiant)
    
    def name(self):
        js = eval(self.serie_json)
        return str(js["original_name"])

    def __str__(self):
        return str(self.serie_identifiant)

    def photo(self):
        js = eval(self.serie_json)
        path = js["poster_path"]
        urllink = "https://image.tmdb.org/t/p/w500/"+str(path) 
        return urllink

    def overview(self):
        js = eval(self.serie_json)
        res = js["overview"]
        if res =="":
            return "Sorry, no overview was available in our database 😢"
        else : 
            return res

    def listSaison(self):
        js = eval(self.serie_json)
        nbSaison = int(js["number_of_seasons"])
        l=[]
        for i in range(nbSaison):
            l.append("Saison "+ str(i+1))
        return l

    def creator(self):
        js = eval(self.serie_json)
        a = js["created_by"]
        res = []
        for i in range(len(a)):
            res.append(a[i]["name"])
        #res = JSserie(self.serie_identifiant)["created_by"][0]["name"]
        if len(res) ==0:
            return "Sorry, no creator was in our database"
        else : 
            return ", ".join(res)

class Season(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    season_text = models.CharField(max_length=200,default ="Noname")
    season_number = models.IntegerField(default = 0)

    def name(self):
        return nomSaison(self.serie.serie_identifiant, self.season_identifiant)

#     def __str__(self):
#         return str(self.season_text, self.season_number)

#     def photo2(self):
#          return photoSaison(self.serie.serie_identifiant,self.season_number)

 
#     def overview2(self):
#         res = JSSaison(self.serie.serie_identifiant,self.season_number)["overview"]
#         if res =="":
#             return "Sorry, no overview was available in our database 😢"
#         else : 
#             return res

    # def listEpisode(self):
    #     nbEpisode = JSSaison(self.season_identifiant)
    #     l=[]
    #     for i in range(nbEpisode):
    #         l.append("Episode "+ str(i+1))
        # return l

# # class Episode(models.Model):
# #     season = models.ForeignKey(Season, on_delete=models.CASCADE) #Cet épisode appartient à une saison spécifique
# #     episode_text = models.CharField(max_length=200,default ="Noname")
# #     episode_identifiant = models.IntegerField(default = 0)

# #     def name(self):
# #         return nom(self.episode_identifiant)

# #     def __str__(self):
# #         return str(self.episode_text)

# #     def photo(self):
# #          return photo(self.episode_identifiant)

# #     def overview(self):
# #         res = JSepisode(self.episode_identifiant)["overview"]
# #         if res =="":
# #             return "Sorry, no overview was available in our database 😢"
# #         else : 
# #             return res






