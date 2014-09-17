import os
import sqlite3
import cgi, cgitb
import shutil, pickle

from django import forms
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.http import HttpResponse
from django.core.files import File
from django.core.context_processors import csrf
from os import path, access, R_OK
from django.shortcuts import render_to_response
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
categories = ["world","sports","business","politics","media","technology","lifestyle"]
linkCategories = ["World","Sports","Business","Politics","Media","Technology","Lifestyle"]
color = ["#08B41C","#089EB4","#872944","#E11A24","#F87C17","#8252EF", "#1AE181"]
marginleft=["530px","850px","15%","530px","850px","15%"]
marginleft1=["532px","852px","15.1%","532px","852px","15.1%"]
top=["420px","420px","780px","780px","780px","1140px"]
top1=["650px","650px","1010px","1010px","1010px","1380px"]
    
def handle_uploaded_file(f):
    with open("C:/Python27/Lib/site-packages/django/contrib/admin/static/admin/img/bg14.jpg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
class EForm(forms.Form):
    author = forms.CharField(max_length=100)
    heading = forms.CharField()
    content = forms.CharField()
    image  = forms.FileField()
    
def save(request):
    imgpath = "C:/Python27/Lib/site-packages/django/contrib/admin/static/admin/img/"
    Path =  settings.STATIC_ROOT+"/ceryx/"
    shutil.copyfile(Path+"Author.txt",Path+"AuthorO.txt")
    shutil.copyfile(Path+"Heading.txt",Path+"HeadingO.txt")
    shutil.copyfile(Path+"Content.txt",Path+"ContentO.txt")
    shutil.copyfile(imgpath+"bg14.jpg",imgpath+"bg15.jpg")
    if request.method=="POST":
        form = EForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.cleaned_data["author"]
            heading  = form.cleaned_data["heading"]
            content  = form.cleaned_data["content"]
            handle_uploaded_file(request.FILES["image"])
            a = open("Author.txt", "w")
            h = open("Heading.txt", "w")
            c = open("Content.txt", "w")
            a.write(str(author))
            h.write(str(heading))
            c.write(str(content))
            html="EDITORIAL SAVED SUCESSFULLY"
        else:
            html="ERROR in INPUT"
    else:
        html = "ERROR"
    return HttpResponse(html)
    
def editorialContent(filename):
    Path =  settings.STATIC_ROOT + "/ceryx/" + filename 
    c=""
    if path.exists(Path) and path.isfile(Path) and access(Path, R_OK):
        f = open(Path, "r")
        myfile = File(f)
        for line in myfile:
            c = c + line
        myfile.closed
        f.closed
    else:
        c="ERROR"
    return (c)

def indiv(pathname,cat):
    PATH =  settings.STATIC_ROOT+"/story/"+cat+"/"
    c=""
    Path=PATH+"/"+str(pathname)+'.html'
    f = pickle.load(open(Path, "rb"))
    return (f)

def story(cat):
    PATH =  settings.STATIC_ROOT+"/story/"+cat+"/"
    story = []    
    for i in range(1,7):
        c=""
        Path=PATH+str(i)+'.html'
        if path.exists(Path) and path.isfile(Path) and access(Path, R_OK):
            f = open(Path, "rb")
            myfile = File(f)
            for line in myfile:
                c = c + line
            myfile.closed
            f.closed
            story.append(c)
        else:
            f = open(settings.STATIC_ROOT+"/story/story.html","w")
            f.write(c)
            break
    return (story)

def front(table,column):
    con = sqlite3.connect(settings.STATIC_ROOT+"/dbtrends.db")
    cursor = con.cursor()
    cursor.execute("Select " + column +" from " + table)
    a = cursor.fetchall()
    b=[]
    for i in a:
        b.append(i[0])
    return (b)

def trend(table):
    con = sqlite3.connect(settings.STATIC_ROOT+"/dbtrends.db")
    cursor = con.cursor()
    cursor.execute("Select trend from " + table)
    a = cursor.fetchall()
    b=[]
    for i in a:
        b.append(i[0])
    return (b)

def headlines(table):
    con = sqlite3.connect(settings.STATIC_ROOT+"/dbtrends.db")
    cursor = con.cursor()
    cursor.execute("Select source from " + table)
    a = cursor.fetchall()
    b=[]
    for i in a:
        b.append(i[0])
    return (b)
    
def links(table):
    con = sqlite3.connect(settings.STATIC_ROOT+"/dbtrends.db")
    cursor = con.cursor()
    cursor.execute("Select link from " + table)
    a = cursor.fetchall()
    b=[]
    for i in a:
        b.append(i[0])
    return (b)

def world(request):
    t = get_template("category.html")
    headline = headlines("world")
    news = trend("world")
    link = links("world")    
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    boxcolor = ["#08B41C","#323433","#08B41C","#323433","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#08B41C","#FFFFFF","#08B41C","#3F8C48","#3F8C48"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#3F8C48","#3F8C48"]
    html = t.render(RequestContext(request,{'title':"World",'theme':"#08B41C",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"AROUND THE WORLD",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def politics(request):
    t = get_template("category.html")
    headline = headlines("politics")
    news = trend("politics")
    link = links("politics")
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    boxcolor = ["#E11A24","#010101","#E11A24","#010101","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#E11A24","#FFFFFF","#E11A24","#F9605D","#F9605D"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#F9605D","#F9605D"]
    html = t.render(RequestContext(request,{'title':"Politics",'theme':"#E11A24",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"POLITICS",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def tech(request):
    t = get_template("category.html")
    headline = headlines("technology")
    news = trend("technology")
    link = links("technology")
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    boxcolor = ["#8252EF","#323434","#8252EF","#323434","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#8252EF","#FFFFFF","#8252EF","#3B03BB","#3B03BB"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#3B03BB","#3B03BB"]
    html = t.render(RequestContext(request,{'title':"Tech",'theme':"#8252EF",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"TECHNOLOGY",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def life(request):
    t = get_template("category.html")
    headline = headlines("living")
    news = trend("living")
    link = links("living")
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    boxcolor = ["#1AE181","#212121","#1AE181","#212121","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#1AE181","#FFFFFF","#1AE181","#027664","#027664"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#027664","#027664"]
    html = t.render(RequestContext(request,{'title':"Lifestyle",'theme':"#1AE181",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"LIFESTYLE",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def business(request):
    t = get_template("category.html")
    headline = headlines("business")
    news = trend("business")
    link = links("business")
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    boxcolor = ["#872944","#030303","#872944","#030303","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#F7C8F3","#FFFFFF","#F7C8F3","#872944","#872944"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#872944","#872944"]
    html = t.render(RequestContext(request,{'title':"Business",'theme':"#872944",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"BUSINESS",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def sports(request):
    t = get_template("category.html")
    headline = headlines("sports")
    news = trend("sports")
    link = links("sports")
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    boxcolor = ["#089EB4","#030303","#089EB4","#030303","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#089EB4","#FFFFFF","#089EB4","#397579","#397579"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#397579","#397579"]
    html = t.render(RequestContext(request,{'title':"Sports",'theme':"#089EB4",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"SPORTS",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def media(request):
    t = get_template("category.html")
    headline = headlines("media")
    news = trend("media")
    link = links("media")
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    boxcolor = ["#F87C17","#6E7070","#F87C17","#6E7070","#FFFFFF","#FFFFFF"]
    fontcolor = ["#FFFFFF","#FBDD1F","#FFFFFF","#FBDD1F","#F87C17","#F87C17"]
    border =["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#F87C17","#F87C17"]
    html = t.render(RequestContext(request,{'title':"Media",'theme':"#F87C17",'marginleft1':marginleft1,'marginleft':marginleft,'top':top,'top1':top1,'color':color,'categories':categories,'category':"MEDIA & ARTS",'border':border,'bgcolor':bgcolor,'news':news, 'headline':headline, 'boxcolor':boxcolor, 'fontcolor':fontcolor}))
    return HttpResponse(html)

def editorial(request):
    t = get_template("editorial.html")
    html = t.render(RequestContext(request,{'color':color,'categories':categories}))
    return HttpResponse(html)

def blog(request):
    t = get_template("blog.html")
    html = t.render(RequestContext(request,{'color':color,'categories':categories}))
    return HttpResponse(html)

def ourTech(request):
    t = get_template("ourTechnology.html")
    html = t.render(RequestContext(request,{'color':color,'categories':categories}))
    return HttpResponse(html)

def aboutUs(request):
    t = get_template("aboutUs.html")
    html = t.render(RequestContext(request,{'color':color,'categories':categories}))
    return HttpResponse(html)

def lifestyle1(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[0]
    td = trend("living")
    trd = td[0]
    story = indiv("1","living")
    l = links("living")
    link = l[0]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def lifestyle2(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[1]
    td = trend("living")
    trd = td[1]
    story = indiv("2","living")
    l = links("living")
    link = l[1]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def lifestyle3(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[2]
    td = trend("living")
    trd = td[2]
    story = indiv("3","living")
    l = links("living")
    link = l[2]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def lifestyle4(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[3]
    td = trend("living")
    trd = td[3]
    story = indiv("4","living")
    l = links("living")
    link = l[3]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def lifestyle5(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[4]
    td = trend("living")
    trd = td[4]
    story = indiv("5","living")
    l = links("living")
    link = l[4]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def lifestyle6(request):
    t = get_template("inside.html")
    h = headlines("living")
    headline = h[5]
    td = trend("living")
    trd = td[5]
    story = indiv("6","living")
    l = links("living")
    link = l[5]
    bgcolor = ["#027664","#027664","#027664","#027664","#027664","#027664","#1AE181"]
    fontcolor = "#212121"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#1AE181",'categories':categories,'category':"LIFESTYLE",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech1(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[0]
    td = trend("technology")
    trd = td[0]
    story = indiv("1","tech")
    l = links("technology")
    link = l[0]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech2(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[1]
    td = trend("technology")
    trd = td[1]
    story = indiv("2","tech")
    l = links("technology")
    link = l[1]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech3(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[2]
    td = trend("technology")
    trd = td[2]
    story = indiv("3","tech")
    l = links("technology")
    link = l[2]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech4(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[3]
    td = trend("technology")
    trd = td[3]
    story = indiv("4","tech")
    l = links("technology")
    link = l[3]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech5(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[4]
    td = trend("technology")
    trd = td[4]
    story = indiv("5","tech")
    l = links("technology")
    link = l[4]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def tech6(request):
    t = get_template("inside.html")
    h = headlines("technology")
    headline = h[5]
    td = trend("technology")
    trd = td[5]
    story = indiv("6","tech")
    l = links("technology")
    link = l[5]
    bgcolor = ["#3B03BB","#3B03BB","#3B03BB","#3B03BB","#3B03BB","#8252EF","#3B03BB"]
    fontcolor = "#3B03BB"
    line = "#323434"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#8252EF",'categories':categories,'category':"TECHNOLOGY",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media1(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[0]
    td = trend("media")
    trd = td[0]
    story = indiv("1","media")
    l = links("media")
    link = l[0]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA & ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media2(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[1]
    td = trend("media")
    trd = td[1]
    story = indiv("2","media")
    l = links("media")
    link = l[1]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA & ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media3(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[2]
    td = trend("media")
    trd = td[2]
    story = indiv("3","media")
    l = links("media")
    link = l[2]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA & ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media4(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[3]
    td = trend("media")
    trd = td[3]
    story = indiv("4","media")
    l = links("media")
    link = l[3]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA & ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media5(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[4]
    td = trend("media")
    trd = td[4]
    story = indiv("5","media")
    l = links("media")
    link = l[4]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA & ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def media6(request):
    t = get_template("inside.html")
    h = headlines("media")
    headline = h[5]
    td = trend("media")
    trd = td[5]
    story = indiv("6","media")
    l = links("media")
    link = l[5]
    bgcolor = ["#FBDD1F","#FBDD1F","#FBDD1F","#FBDD1F","#F87C17","#FBDD1F","#FBDD1F"]
    fontcolor = "#FBDD1F"
    line = "#6E7070"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#F87C17",'categories':categories,'category':"MEDIA AND ARTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business1(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[0]
    td = trend("business")
    trd = td[0]
    story = indiv("1","biz")
    l = links("business")
    link = l[0]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business2(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[1]
    td = trend("business")
    trd = td[1]
    story = indiv("2","biz")
    l = links("business")
    link = l[1]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business3(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[2]
    td = trend("business")
    trd = td[2]
    story = indiv("3","biz")
    l = links("business")
    link = l[2]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business4(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[3]
    td = trend("business")
    trd = td[3]
    story = indiv("4","biz")
    l = links("business")
    link = l[3]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business5(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[4]
    td = trend("business")
    trd = td[4]
    story = indiv("5","biz")
    l = links("business")
    link = l[4]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def business6(request):
    t = get_template("inside.html")
    h = headlines("business")
    headline = h[5]
    td = trend("business")
    trd = td[5]
    story = indiv("6","biz")
    l = links("business")
    link = l[5]
    bgcolor = ["#F7C8F3","#F7C8F3","#872944","#F7C8F3","#F7C8F3","#F7C8F3","#F7C8F3"]
    fontcolor = "#F7C8F3"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#872944",'categories':categories,'category':"BUSINESS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports1(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[0]
    td = trend("sports")
    trd = td[0]
    story = indiv("1","sports")
    l = links("sports")
    link = l[0]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports2(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[1]
    td = trend("sports")
    trd = td[1]
    story = indiv("2","sports")
    l = links("sports")
    link = l[1]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports3(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[2]
    td = trend("sports")
    trd = td[2]
    story = indiv("3","sports")
    l = links("sports")
    link = l[2]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports4(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[3]
    td = trend("sports")
    trd = td[3]
    story = indiv("4","sports")
    l = links("sports")
    link = l[3]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports5(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[4]
    td = trend("sports")
    trd = td[4]
    story = indiv("5","sports")
    l = links("sports")
    link = l[4]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def sports6(request):
    t = get_template("inside.html")
    h = headlines("sports")
    headline = h[5]
    td = trend("sports")
    trd = td[5]
    story = indiv("6","sports")
    l = links("sports")
    link = l[5]
    bgcolor = ["#397579","#089EB4","#397579","#397579","#397579","#397579","#397579"]
    fontcolor = "#397579"
    line = "#030303"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#089EB4",'categories':categories,'category':"SPORTS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics1(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[0]
    td = trend("politics")
    trd = td[0]
    story = indiv("1","politics")
    l = links("politics")
    link = l[0]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics2(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[1]
    td = trend("politics")
    trd = td[1]
    story = indiv("2","politics")
    l = links("politics")
    link = l[1]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics3(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[2]
    td = trend("politics")
    trd = td[2]
    story = indiv("3","politics")
    l = links("politics")
    link = l[2]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics4(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[3]
    td = trend("politics")
    trd = td[3]
    story = indiv("4","politics")
    l = links("politics")
    link = l[3]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics5(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[4]
    td = trend("politics")
    trd = td[4]
    story = indiv("5","politics")
    l = links("politics")
    link = l[4]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def politics6(request):
    t = get_template("inside.html")
    h = headlines("politics")
    headline = h[5]
    td = trend("politics")
    trd = td[5]
    story = indiv("6","politics")
    l = links("politics")
    link = l[5]
    bgcolor = ["#F9605D","#F9605D","#F9605D","#E11A24","#F9605D","#F9605D","#F9605D"]
    fontcolor = "#F9605D"
    line = "#010101"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#E11A24",'categories':categories,'category':"POLITICS",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world1(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[0]
    td = trend("world")
    trd = td[0]
    story = indiv("1","world")
    l = links("world")
    link = l[0]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world2(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[1]
    td = trend("world")
    trd = td[1]
    story = indiv("2","world")
    l = links("world")
    link = l[1]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'link':link, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world3(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[2]
    td = trend("world")
    trd = td[2]
    story = indiv("3","world")
    l = links("world")
    link = l[2]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'link':link,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world4(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[3]
    td = trend("world")
    trd = td[3]
    story = indiv("4","world")
    l = links("world")
    link = l[3]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'link':link,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world5(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[4]
    td = trend("world")
    trd = td[4]
    story = indiv("5","world")
    l = links("world")
    link = l[4]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'link':link,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)

def world6(request):
    t = get_template("inside.html")
    h = headlines("world")
    headline = h[5]
    td = trend("world")
    trd = td[5]
    story = indiv("6","world")
    l = links("world")
    link = l[5]
    bgcolor = ["#08B41C","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48","#3F8C48"]
    fontcolor = "#3F8C48"
    line = "#323433"
    html = t.render(RequestContext(request,{'trend':trd,'link':link,'theme':"#08B41C",'categories':categories,'category':"AROUND THE WORLD",'line':line,'bgcolor':bgcolor, 'headline':headline, 'fontcolor':fontcolor, 'story':story}))
    return HttpResponse(html)
                    
def index(request):
    t = get_template("index.html")
    w=front("world","source")
    p=front("politics","source")
    c=front("technology","source")
    l=front("living","source")
    b=front("business","source")
    s=front("sports","source")
    m=front("media","source")
    trends=trend("trends")
    author=editorialContent("Author.txt")
    heading=editorialContent("Heading.txt")
    content=editorialContent("Content.txt")
    authorO=editorialContent("AuthorO.txt")
    headingO=editorialContent("HeadingO.txt")
    contentO=editorialContent("ContentO.txt")
    html = t.render(RequestContext(request,{'color':color,'categories':categories,'heading':heading,'author':author,'content':content,'headingO':headingO,'authorO':authorO,'contentO':contentO,'trends':trends,'worldh':w[0],'businessh':b[0],'politicsh':p[0],'sportsh':s[0],'techh':c[0], 'lifeh':l[0], 'mediah':m[0]}))
    #html = t.render(RequestContext(request,{'color':color,'categories':categories,'heading':heading,'author':author,'content':content,'headingO':headingO,'authorO':authorO,'contentO':contentO,'trends':trends,'worldh':w[0][0],'businessh':b[0][0],'politicsh':p[0][0],'sportsh':s[0][0],'techh':c[0][0], 'lifeh':l, 'mediah':m[0][0]}))
    return HttpResponse(html)
