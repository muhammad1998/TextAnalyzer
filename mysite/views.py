from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    removenewline = request.POST.get('removenextline','off')
    removewidespace = request.POST.get('removewidespace','off')
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if removepunc=='on':
        
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        param = {'purpose':'Remove Punctuation','analyzed': analyzed}
        djtext =analyzed
    if uppercase == 'on':
        analyzed = djtext.upper()
        param = {'purpose':'Upper Case','analyzed': analyzed}
        djtext=analyzed
    if removenewline == 'on':
        analyzed = ""
        for char in djtext:
            if(char!="\n" and char!="\r"):
                analyzed = analyzed+char
        param = {'purpose':'Remove Newline','analyzed': analyzed}    
        djtext=analyzed
    if removewidespace == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==' 'and djtext[index+1]==' '):
                analyzed+=char  
        param = {'purpose':'Remove Extra Space','analyzed': analyzed}
        djtext = analyzed



    
    return render(request,'analyzetext.html',param)
