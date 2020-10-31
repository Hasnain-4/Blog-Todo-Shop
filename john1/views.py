from django.shortcuts import render, redirect
from .models import Post
import requests
from django.contrib import messages

import json
from newsapi import NewsApiClient

from .forms import PostForm

# Create your views here.

def home(request):
    allposts = Post.objects.all()
    
    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='techcrunch')
    articles = topheadlines['articles']

    auth=[]
    tit=[]
    pub=[]
    url=[]

# print(json.dumps(json_response,indent=2))
    for i in range(len(articles)):
        myarticles = articles[i]
        auth.append(myarticles['author'])
        tit.append(myarticles['title'])
        pub.append(myarticles['publishedAt'])
        url.append(myarticles['description'])
    # print(author,title,publishedAt )
        data = zip(auth,tit,pub,url)

    return render(request, 'home.html', {'posts':allposts,'data':data})

def myposts(request):
    allposts = Post.objects.all()
    
    if request.method == 'POST':
        ptitle = request.POST.get('title')
        pdesc = request.POST.get('desc')
        pimg = request.FILES.get('img')

        pos = Post(title = ptitle, desc=pdesc,image = pimg)
        pos.save()
        messages.success(request, "Post Added Successfully")

    return render(request, 'myposts.html', {'posts':allposts})

def about(request):

    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def addpost(request):

    return render(request, 'addpost.html')

def edit_post(request, id):

    if request.method == 'POST':

        pi = Post.objects.get(pk=id)
        form = PostForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated Successfully")
            return redirect('myposts')

    else:
        pi = Post.objects.get(pk=id)
        form = PostForm(instance=pi)
    return render(request, 'edit_post.html', {'form':form})

def delete_post(request, id):
    post_to_delete=Post.objects.get(id=id)
    post_to_delete.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('myposts')
 #   return render(request, 'myposts.html')