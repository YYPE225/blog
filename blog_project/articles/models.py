from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='articles')
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur.username} - {self.contenu[:20]}"
