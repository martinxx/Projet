Ceci est la notice d'utilisation du projet "Webserie" en python par le groupe:
Decroix Martin, Bonnet Charles & Damerdji Malik Kamel

I Prérequis logiciels
II Lancer et utliser l'application
III Quels fichiers doivent être évalués?

I Prérequis logiciels : 

* Le projet est fait pour tourner sous python 3.5.2 . Il devrait théoriquement également fonctionner sous python 3.2
* Le projet ne fonctionne pas sous python 2 (différent nommage de la bibliothèque Urllib)
* Le projet requiert l'installation du framework python Django, version 1.10.2 ou ultérieure. Pour cela plusieurs possibilités: 
	[recommandé] la commande pip install Django  (ou pip install Django==1.10.2 pour être sûr d'avoir la même version que nous)
	l'installer depuis git:  $ git clone git://github.com/django/django.git puis exécuter la commande pip install -e django:


Pour verifier que l'installation de django est correcte, utiliser la commande python -m django --version. 
Si la réponse est 1.10.2 ou ultérieure , django est correctement installé.
En cas de soucis : https://docs.djangoproject.com/fr/1.10/topics/install/#installing-official-release


II Lancer l'application :
Sur votre terminal ou Windows Powershell, placez vous dans le répertoire du projet (ce repertoire doit contenir un fichier python appelé "manage", extension .py ).
Lancez la commande python manage.py runserver.
Ouvrez un navigateur web et entrez l'url http://127.0.0.1:8000/webseries/
Vous pouvez à présent tester l'application sur votre navigateur

L'application vous permet de: 
* créer un compte à votre nom (sans protection par mot de passe)
* y ajouter une série en entrant un nom ressemblant (en anglais) (si le nom n'est pas exact mais approchant, la série doit quand même être trouvée).
* Regarder pour chaque série de son compte la liste des saisons, des épisodes, et le nom et la date de diffusion du prochain épisode de la saison si celle-ci est encore en cours de diffusion.


III Quels fichiers doivent être évalués?

Voici les fichiers que nous avons écris :
Répertoire projet : 
Projet API.py (notre bibliothèque de fonctions)
Répertoire projet/webseries : (les fichiers de ce répértoire ont été écrits par nous à partir d'un template vierge fourni par django)
admin.py (configure la gestion de la page admin)
apps.py (nom de l'application)
models.py (nos classes)
url.py (nos adresses url)
views.py (nos vues)
Répertoire projet/webseries/templates/webseries :
Tous nos fichiers html 
Répertoire projet/webséries/static: 
Tous nos fichiers CSS

Les autres fichiers sont fournis par Django et n'ont pas été modifiés par nous.

