from django.core.files import File
from os import path, access, R_OK

def editorialContent(filename):
    Path = "C://Python27/mysite/ceryx/" + filename  
    c=""
    if path.exists(Path) and path.isfile(Path) and access(Path, R_OK):
        f = open(Path, "r")
        myfile = File(f)
        for line in myfile:
            c = c + line
        myfile.closed
        f.closed
    else:
        econtent.append("ERROR")
    return (c)

print editorialContent("Content.txt")
