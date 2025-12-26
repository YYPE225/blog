from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.liste_articles, name='liste'),
    path('<int:id>/', views.detail_article, name='detail'),
    path('creer/', views.creer_article, name='creer'),
    path('<int:article_id>/commentaire/', views.ajouter_commentaire,
         name='ajouter_commentaire'),
    path('<int:id>/modifier/', views.modifier_article, name='modifier'),
    path('<int:id>/supprimer/', views.supprimer_article, name='supprimer'),
    path('commentaire/<int:id>/modifier/', views.modifier_commentaire,
         name='modifier_commentaire'),
    path('commentaire/<int:id>/supprimer/', views.supprimer_commentaire,
         name='supprimer_commentaire'),

]
