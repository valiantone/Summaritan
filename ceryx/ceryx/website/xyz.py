import os
import sqlite3

from django.template.loader import get_template
from django.template import RequestContext, Context
from django.http import HttpResponse
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
from django.http import HttpResponse
from django.core.files import File
from os import path, access, R_OK

def test():
    PATH = "C://Python27/mysite/TEST/"
    story = []    
    for i in range(1,7):
        c=" "
        Path=PATH+str(i)+'.txt'
        if path.exists(Path) and path.isfile(Path) and access(Path, R_OK):
            f = open(Path, "r")
            myfile = File(f)
            for line in myfile:
                c = c + line
            myfile.closed
            f.closed
            story.append(c)
        else:
            f = open("C://Python27/mysite/TEST/story.html","w")
            f.write(c)
            break
    print story
    return
test()
