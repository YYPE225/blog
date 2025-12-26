from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Commentaire
from .forms import ArticleForm
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def liste_articles(request):
    articles = Article.objects.all().order_by('-date_creation')
    return render(request, 'articles/liste.html', {'articles': articles})


def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    commentaires = article.commentaires.all().order_by('-date_creation')
    return render(request, 'articles/detail.html', {
        'article': article,
        'commentaires': commentaires
    })


@login_required
def creer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            return redirect('articles:liste')
    else:
        form = ArticleForm()
    return render(request, 'articles/creer.html', {'form': form})


def ajouter_commentaire(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = CommentaireForm()
    return render(request, 'articles/ajouter_commentaire.html', {
        'form': form,
        'article': article
    })


@login_required
def modifier_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user != article.auteur:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier cet article.")
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/modifier.html', {'form': form,
                                                      'article': article})


@login_required
def supprimer_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user != article.auteur:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer cet article.")
    if request.method == 'POST':
        article.delete()
        return redirect('articles:liste')
    return render(request, 'articles/supprimer.html', {'article': article})


@login_required
def modifier_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)

    if commentaire.auteur != request.user:
        return HttpResponseForbidden("Accès interdit")

    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=commentaire.article.id)
    else:
        form = CommentaireForm(instance=commentaire)

    return render(request, 'articles/modifier_commentaire.html',
                  {'form': form, 'commentaire': commentaire})


@login_required
def supprimer_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)

    if commentaire.auteur != request.user:
        return HttpResponseForbidden("Accès interdit")

    article_id = commentaire.article.id
    if request.method == 'POST':
        commentaire.delete()
        return redirect('articles:detail', id=article_id)

    return render(request, 'articles/supprimer_commentaire.html',
                  {'commentaire': commentaire})
