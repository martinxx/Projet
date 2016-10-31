import json
import urllib.request
import smtplib
from datetime import date
from django.db import models

key = "5c3fde1ab28b3cb007c61d944b4d4c94"


def nom(js):
    """Renvoie le nom de la série"""
    resultat = js["original_name"] 
    return resultat
