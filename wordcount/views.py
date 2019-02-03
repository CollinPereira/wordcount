from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')


def count(request):
    words=request.GET['words']
    wordlist=words.split()
    cnt={}
    for word in wordlist:
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word]=1
    sorted_words=sorted(cnt.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'words':words,'length':len(wordlist),'sorted_words':sorted_words})   
