import urllib2, urllib,requests
from operator import itemgetter
import re, sqlite3,json, datetime
from requests_oauthlib import OAuth1
global tweet
trendList=[]
Sports=[]
Politics=[]
Media=[]
World=[]
Living=[]
Business=[]
Technology=[]

oauth = OAuth1("WJhLi0byCbnbVHjqRElsYQ",
                client_secret="PHgutrqxiAQ1ahZPrHf1qhudTTnXXMzGsnxSL1L50lc",
                resource_owner_key="54203379-eO801AwvLtFxID5x42qRXmJgjx0S2VCUZd7AqkPus",
                resource_owner_secret="Av70QJeZqezMaHeqr61wlRVfqnDHQ9uFsnKrlmUJb0")

def polPop():
    nc=0
    tc=0
    hc=0
    oc=0
    ec=0
    global Politics, oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=E_P_W",auth=oauth)
    e = data.json()
    head=e[ec]["text"]
    link=re.findall(r'(https?://\S+)', head)
    x="https://www.facebook.com"
    while link==[] or x in requests.get(link[0]).url:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("Economic and Political Weekly",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Tehelka",auth=oauth)
    t = data.json()
    head=t[tc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("Tehelka",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=thecaravanindia",auth=oauth)
    h = data.json()
    head=h[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("The Caravan",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=ndtv",auth=oauth)
    n = data.json()
    head=n[nc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("NDTV",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=t[tc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("Tehelka",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Openthemag",auth=oauth)
    o = data.json()
    head=o[oc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        oc+=1
        head=o[oc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Politics.append(("Open The Magazine",head[:-len(link[0])-1], requests.get(link[0]).url))

def techPop():
    wc=0
    tc=0
    vc=0
    global Technology,oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Gizmodo",auth=oauth)
    w = data.json()
    head=w[wc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("Gizmodo",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=TechRepublic", auth=oauth)
    t = data.json()
    head=t[tc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("TechRepublic",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=techreview", auth=oauth)
    v = data.json()
    head=v[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        vc+=1
        head=v[vc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("MIT Tech review",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=w[wc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("Gizmodo",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=t[tc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        tc+=1
        head=t[tc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("TechRepublic",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=v[vc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        vc+=1
        head=v[vc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Technology.append(("MIT Tech Review",head[:-len(link[0])-1], requests.get(link[0]).url))

def lvgPop():
    cc=0
    hc=0
    gc=0
    global Living,oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=RtrsIN_Life", auth=oauth)
    c = data.json()
    head=c[cc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        cc+=1
        head=c[cc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("Reuters India Life",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=USATODAYhealth",auth=oauth)
    h = data.json()
    head=h[hc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("USA Today Health",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=ForbesLife", auth=oauth)
    g = data.json()
    head=g[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        gc+=1
        head=g[gc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("Forbes Lifestyle",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=c[cc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        cc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("Reuters India Life",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=h[hc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        hc+=1
        head=h[hc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("USA Today Health",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=g[gc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        gc+=1
        head=g[gc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Living.append(("Forbes Lifestyle",head[:-len(link[0])-1], requests.get(link[0]).url))

def bizPop():
    bc=0
    ec=0
    nc=0
    wc=0
    kc=0
    fc=0
    global Business, oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=bsindia", auth=oauth)
    b = data.json()
    head=b[bc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        bc+=1
        head=b[bc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("Business Standard",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=TheEconomist", auth=oauth)
    e = data.json()
    head=e[ec]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("The Economist",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=nytimesbusiness", auth=oauth)
    n = data.json()
    head=n[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("NYTimes Business",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=RtrsIN_Business", auth=oauth)
    w = data.json()
    head=w[wc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("Reuters India Business",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=livemint",auth=oauth)
    k = data.json()
    head=k[kc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        kc+=1
        head=k[kc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("Livemint",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=EconomicTimes", auth=oauth)
    f = data.json()
    head=f[fc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Business.append(("Economic Times",head[:-len(link[0])-1], requests.get(link[0]).url))

def sptPop():
    fc=0
    ec=0
    nc=0
    sc=0
    cc=0
    bc=0
    global Sports, oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=HuffPostUKSport", auth=oauth)
    f = data.json()
    head=f[fc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("Huffington Post Sports UK",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=guardian_sport", auth=oauth)
    s = data.json()
    head=s[sc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        sc+=1
        head=s[sc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("Guardian Sport",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=USATodaysports", auth=oauth)
    e = data.json()
    head=e[ec]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("USA Today Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=e[ec+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ec+=1
        head=e[ec]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("USA Today Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Sports_NDTV", auth=oauth)
    n = data.json()
    head=n[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("NDTV Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

    head=n[nc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        nc+=1
        head=n[nc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    Sports.append(("NDTV Sports",head[:-len(link[0])-1], requests.get(link[0]).url))

def wldPop():
    uc=0
    fc=0
    bc=0
    ac=0
    sc=0
    wc=0
    global World, oauth
    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=USATODAY", auth=oauth)
    u = data.json()
    head=u[uc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        uc+=1
        head=u[uc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("USA Today",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=washingtonpost", auth=oauth)
    f = data.json()
    head=f[fc]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        fc+=1
        head=f[fc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("Washington Post",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BBCNews", auth=oauth)
    b = data.json()
    head=b[0]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        bc+=1
        head=b[bc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("BBC UK",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=HuffingtonPost", auth=oauth)
    a = data.json()
    head=a[ac+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        ac+=1
        head=a[ac]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("Huffington Post",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=ReutersWorld", auth=oauth)
    s = data.json()
    head=s[sc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        sc+=1
        head=s[sc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("Reuters",head[:-len(link[0])-1], requests.get(link[0]).url))

    data = requests.get(url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BBCWorld", auth=oauth)
    w = data.json()
    head=w[wc+1]["text"]
    link=re.findall(r'(https?://\S+)', head)
    while link==[]:
        wc+=1
        head=w[wc]["text"]
        link=re.findall(r'(https?://\S+)', head)
    print head
    World.append(("BBC World",head[:-len(link[0])-1], requests.get(link[0]).url))

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
print
print "Politics Trends Recorded"
print
wldPop()
print
print "World Trends Recorded"
print
sptPop()
print
print "Sports Trends Recorded"
print
bizPop()
print
print "Business Trends Recorded"
print
techPop()
print
print "Technology Trends Recorded"
print
lvgPop()
print
print "Living Trends Recorded"
print
writeTrends()
