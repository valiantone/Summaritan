import urllib2, urllib, blekko, requests
from operator import itemgetter
import re, sqlite3, twitter, json, datetime

trendList=[]
Sports=[]
Politics=[]
Media=[]
World=[]
Living=[]
Business=[]
Technology=[]

def polPop():
    nc=0
    tc=0
    hc=0
    global Politics
    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=ndtv").read()
    n = json.loads(data)
    print n
    head=n[nc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("NDTV",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=tehelkadotcom").read()
    t = json.loads(data)
    head=t[tc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("Tehelka",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=TheHindu").read()
    h = json.loads(data)
    head=h[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("The Hindu",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=n[nc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("NDTV",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=t[tc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("Tehelka",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=h[hc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Politics.append(("The Hindu",head[:-len(link[0])-1], requests.get(link[0]).url))

def wldPop():
    uc=0
    fc=0
    bc=0
    ac=0
    sc=0
    wc=0
    global World
    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=USATODAY").read()
    u = json.loads(data)
    head=u[uc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        uc+=1
        head=u[uc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("USA Today",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=washingtonpost").read()
    f = json.loads(data)
    head=f[fc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("Washington Post",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BBCNews").read()
    b = json.loads(data)
    head=b[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        bc+=1
        head=b[bc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("BBC UK",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=HuffingtonPost").read()
    a = json.loads(data)
    head=a[ac+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ac+=1
        head=a[ac]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("Huffington Post",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=ReutersWorld").read()
    s = json.loads(data)
    head=s[sc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        sc+=1
        head=s[sc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("Reuters",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=BBCWorld").read()
    w = json.loads(data)
    head=w[wc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    World.append(("BBC World",head[:-len(link[0])-1], requests.get(link[0]).url))

def sptPop():
    fc=0
    ec=0
    nc=0
    sc=0
    cc=0
    bc=0
    global Sports
    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=HuffPostUKSport").read()
    f = json.loads(data)
    head=f[fc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("Huffington Post Sports UK",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=f[fc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("Huffington Post Sports UK",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=USATodaysports").read()
    e = json.loads(data)
    head=e[ec]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("USA Today Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=e[ec+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("USA Today Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=Sports_NDTV").read()
    n = json.loads(data)
    head=n[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("NDTV Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=n[nc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Sports.append(("NDTV Sports",head[:-len(link[0])-1], requests.get(link[0]).url))


def bizPop():
    bc=0
    ec=0
    nc=0
    wc=0
    kc=0
    fc=0
    global Business
    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=bsindia").read()
    b = json.loads(data)
    head=b[bc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        bc+=1
        head=b[bc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("Business Standard",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=TheEconomist").read()
    e = json.loads(data)
    head=e[ec]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("The Economist",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=nytimesbusiness").read()
    n = json.loads(data)
    head=n[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("NYTimes Business",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=WSJ").read()
    w = json.loads(data)
    head=w[wc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("Wall Street Journal",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=businessweekly").read()
    k = json.loads(data)
    head=k[kc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        kc+=1
        head=k[kc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("Business Weekly",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=FinancialReview").read()
    f = json.loads(data)
    head=f[fc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Business.append(("Financial Review",head[:-len(link[0])-1], requests.get(link[0]).url))

`def lvgPop():
    cc=0
    hc=0
    gc=0
    global Living
    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=RtrsIN_Life").read()
    c = json.loads(data)
    head=c[cc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        cc+=1
        head=c[cc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("Reuters India Life",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=USATODAYhealth").read()
    h = json.loads(data)
    head=h[hc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("USA Today Health",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=ForbesLife").read()
    g = json.loads(data)
    head=g[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        gc+=1
        head=g[gc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("Forbes Lifestyle",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=c[cc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        cc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("Reuters India Life",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=h[hc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("USA Today Health",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=g[gc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        gc+=1
        head=g[gc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    Living.append(("Forbes Lifestyle",head[:-len(link[0])-1], requests.get(link[0]).url))

def writeTrends():
    global trendList,Sports, Living, Media, Politics, World, Business, Technology
    conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn.cursor()
    c.execute('''drop table if exists Politics''')
    c.execute('''create table Politics(Trend text, Source text, Link text)''')
    if len(Politics)<=10:
        x=len(Politics)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into Politics values(?,?,?)", Politics[i])
    conn.commit()
    c.execute('''drop table if exists World''')
    c.execute('''create table World(Trend text, Source text, Link text)''')
    if len(World)<=10:
        x=len(World)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into World values(?,?,?)", World[i])
    conn.commit()
    c.execute('''drop table if exists Sports''')
    c.execute('''create table Sports(Trend text, Source text, Link text)''')
    if len(Sports)<=10:
        x=len(Sports)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into Sports values(?,?,?)", Sports[i])
    conn.commit()
    c.execute('''drop table if exists Business''')
    c.execute('''create table Business(Trend text, Source text, Link text)''')
    if len(Business)<=10:
        x=len(Business)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into Business values(?,?,?)", Business[i])
    conn.commit()
    c.execute('''drop table if exists Technology''')
    c.execute('''create table Technology(Trend text, Source text, Link text)''')
    if len(Technology)<=10:
        x=len(Technology)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into Technology values(?,?,?)", Technology[i])
    conn.commit()
    c.execute('''drop table if exists Living''')
    c.execute('''create table Living(Trend text, Source text, Link text)''')
    if len(Living)<=10:
        x=len(Living)
    else:
        x=10
    for i in range(x):
        c.execute("Insert into Living values(?,?,?)", Living[i])
    conn.commit()
    c.close()

polPop()
print "Politics Trends Recorded"
wldPop()
print "World Trends Recorded"
sptPop()
print "Sports Trends Recorded"
bizPop()
print "Business Trends Recorded"
techPop()
print "Technology Trends Recorded"
lvgPop()
print "Living Trends Recorded"
writeTrends()
    



