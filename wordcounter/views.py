
from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    total = fulltext.split()
    histo={}
    for word in total:
        if word in histo:
            histo[word]+=1
        else:
            histo[word]=1
        sortedwords=sorted(histo.items(), key=operator.itemgetter(1), reverse=True)
    return render(request ,'count.html',{'fulltext':fulltext,'count':len(total) ,'occurance': sortedwords})
def about(request):
    return render(request,'about.html')