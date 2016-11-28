from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	#ex: /webseries/
    url(r'^ajoutCompte/$', views.ajoutCompte, name='ajoutCompte'),
    # ex: /webseries/ajoutCompte/
    url(r'^(?P<account_id>[0-9]+)/$', views.listSerie, name='listSerie'),
	# ex: /webseries/2
    url(r'^(?P<account_id>[0-9]+)/ajoutSerie/$', views.ajoutSerie, name='ajoutSerie'),
	# ex: /webseries/2/ajoutSerie
    url(r'^(?P<account_id>[0-9]+)/ajoutSerie/SelectionSerie/$', views.SelectionSerie, name='SelectionSerie'),
    # ex: /webseries/5/serie/ajouteSerie/SelectionSerie
    url(r'^(?P<account_id>[0-9]+)/serie/(?P<serie_id>[0-9]+)/$', views.listSaison, name='listSaison'),
   # ex: /webseries/5/serie/2
    url(r'^(?P<account_id>[0-9]+)/serie/(?P<serie_id>[0-9]+)/season/(?P<season_id>[0-9]+)$', views.listEpisode, name='listEpisode'),
  # ex: /webseries/5/serie/2/season/12
  # url(r'^/vote/$', views.ajout_compte, name='ajout_compte'),
    url(r'^(?P<account_id>[0-9]+)/serie/(?P<serie_id>[0-9]+)/season/(?P<season_id>[0-9]+)/episode/(?P<episode_id>[0-9]+)/$', views.nameEpisode, name='nameEpisode'),
]