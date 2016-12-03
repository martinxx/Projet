Ceci est la notice d'utilisation du projet "Webserie" en python par le groupe:
Decroix Martin, Bonnet Charles & Damerdji Malik Kamel

I Pr�requis logiciels
II Lancer et utliser l'application
III Quels fichiers doivent �tre �valu�s?

I Pr�requis logiciels : 

* Le projet est fait pour tourner sous python 3.5.2 . Il devrait th�oriquement �galement fonctionner sous python 3.2
* Le projet ne fonctionne pas sous python 2 (diff�rent nommage de la biblioth�que Urllib)
* Le projet requiert l'installation du framework python Django, version 1.10.2 ou ult�rieure. Pour cela plusieurs possibilit�s: 
	[recommand�] la commande pip install Django  (ou pip install Django==1.10.2 pour �tre s�r d'avoir la m�me version que nous)
	l'installer depuis git:  $ git clone git://github.com/django/django.git puis ex�cuter la commande pip install -e django:


Pour verifier que l'installation de django est correcte, utiliser la commande python -m django --version. 
Si la r�ponse est 1.10.2 ou ult�rieure , django est correctement install�.
En cas de soucis : https://docs.djangoproject.com/fr/1.10/topics/install/#installing-official-release


II Lancer l'application :
Sur votre terminal ou Windows Powershell, placez vous dans le r�pertoire du projet (ce repertoire doit contenir un fichier python appel� "manage", extension .py ).
Lancez la commande python manage.py runserver.
Ouvrez un navigateur web et entrez l'url http://127.0.0.1:8000/webseries/
Vous pouvez � pr�sent tester l'application sur votre navigateur

L'application vous permet de: 
* cr�er un compte � votre nom (sans protection par mot de passe)
* y ajouter une s�rie en entrant un nom ressemblant (en anglais) (si le nom n'est pas exact mais approchant, la s�rie doit quand m�me �tre trouv�e).
* Regarder pour chaque s�rie de son compte la liste des saisons, des �pisodes, et le nom et la date de diffusion du prochain �pisode de la saison si celle-ci est encore en cours de diffusion.


III Quels fichiers doivent �tre �valu�s?

Voici les fichiers que nous avons �cris :
R�pertoire projet : 
Projet API.py (notre biblioth�que de fonctions)
R�pertoire projet/webseries : (les fichiers de ce r�p�rtoire ont �t� �crits par nous � partir d'un template vierge fourni par django)
admin.py (configure la gestion de la page admin)
apps.py (nom de l'application)
models.py (nos classes)
url.py (nos adresses url)
views.py (nos vues)
R�pertoire projet/webseries/templates/webseries :
Tous nos fichiers html 
R�pertoire projet/webs�ries/static: 
Tous nos fichiers CSS

Les autres fichiers sont fournis par Django et n'ont pas �t� modifi�s par nous.

