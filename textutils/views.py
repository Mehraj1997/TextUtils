#I have created this file -Mehraj
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def remove(request):
    djtext=request.GET.get('text','default')
    check=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    nlr=request.GET.get('nlr','off')
    esr=request.GET.get('esr','off')
    charactercount=request.GET.get('charcount','off')
    if(check=='on'):
        punctuation ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedText=''
        for c in djtext:
            if c not in punctuation:
                analyzedText+=c;
        param = {'message':'Remove Punctuation','input': analyzedText}
        return render(request, 'analyze.html', param)
    elif(fullcaps=='on'):
        analyzedText=''
        for char in djtext:
            analyzedText+=char.upper()
        param = {'message':'Capitalize the text','input': analyzedText}
        return render(request,'analyze.html',param)
    elif(nlr=='on'):
        analyzedText = ''
        for char in djtext:
            if(char !='\n'):
                analyzedText+=char
        param = {'message':'New Line Remover','input': analyzedText}
        return render(request,'analyze.html',param)
    elif(esr=='on'):
        analyzedText = ''
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzedText+=char
  
        param = {'message':'Extra Space Remover','input': analyzedText}
        return render(request,'analyze.html',param)
    elif(charactercount== 'on'):
        count=0
        
        for char in djtext:
            if(char!=" "):
                count+=1

        param = {'message': 'Extra Space Remover', 'input': count}
        return render(request, 'analyze.html', param)
    else:
        return HttpResponse('Error')

    
    
