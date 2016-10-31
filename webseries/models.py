import datetime
from django.db import models
from django.utils import timezone
from projetAPI import * # Create your models here.

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
    #a = str(serie_identifiant)
    #serie_photo = JSserie(serie_identifiant)

    def name(self):
        return nom(self.serie_identifiant)
        
    @property
    def JSON(self):
        print("$"*500)
        return JSserie(self.serie_identifiant)

    def __str__(self):
        return str(self.serie_identifiant)

    def photo(self):
         return photo(self.serie_identifiant)

    def overview(self):
        res = JSserie(self.serie_identifiant)["overview"]
        if res =="":
            return "Sorry, no overview was available in our database 😢"
        else : 
            return res

    def listSaison(self):
        nbSaison = NbdeSaison(self.serie_identifiant)
        l=[]
        for i in range(nbSaison):
            l.append("Saison "+ str(i+1))
        return l

    def creator(self):
        a = JSserie(self.serie_identifiant)["created_by"]
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
    season_identifiant = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.season_text)



    # def photo(self):
    #      return photo(self.season_identifiant)

    # def numSaison(self):
    #     return int(numSaison(self.serie_identifiant)["season_number"])

    # def overview(self):
    #     res = JSSaison(self.season_identifiant,self.numSaison)["overview"]
    #     if res =="":
    #         return "Sorry, no overview was available in our database 😢"
    #     else : 
    #         return res

    def nbEpsiode(self):
        print("*"*500)
        return("*"*500)


        return l
class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_text = models.CharField(max_length=200,default ="Noname")

    def __str__(self):
        return str(self.season_text)







