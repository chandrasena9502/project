from django.shortcuts import render

def home(requst):
    return render(requst,'index.html')
def first(requst):
    return render(requst,'first.html')