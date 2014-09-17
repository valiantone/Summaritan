import urllib,json, re, blekko, pickle, operator
import reporter
import sqlite3
from collections import defaultdict
from itertools import repeat


Sports=[]
Politics=[]
Media=[]
World=[]
Living=[]
Business=[]
Technology=[]

def extractTrends():
    global Sports, Living, Media, Politics, World, Business, Technology
    conn=sqlite3.connect(r'D:\Summaritan\dbtrends.db')
    c=conn.cursor()
    c.execute('''Select * from Sports''')
    rows = c.fetchall()
    for row in rows:
        Sports.append(row)
    c.execute('''Select * from Politics''')
    rows = c.fetchall()
    for row in rows:
        Politics.append(row)
    c.execute('''Select * from Media''')
    rows = c.fetchall()
    for row in rows:
        Media.append(row)
    c.execute('''Select * from World''')
    rows = c.fetchall()
    for row in rows:
        World.append(row)
    c.execute('''Select * from Living''')
    rows = c.fetchall()
    for row in rows:
        Living.append(row)
    c.execute('''Select * from Business''')
    rows = c.fetchall()
    for row in rows:
        Business.append(row)
    c.execute('''Select * from Technology''')
    rows = c.fetchall()
    for row in rows:
        Technology.append(row)
    conn.commit()
    c.close()

def loadBuilder():
    global Sports, Living, Media, Politics, World, Business, Technology
    load4mSports(Sports)
    load4mLiving(Living)
    #load4mMedia(Media)
    load4mPol(Politics)
    load4mWorld(World)
    load4mBiz(Business)
    load4mTech(Technology)

def load4mSports(alist):
    fp="D:\\Summaritan\\story\\sports\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1


def load4mLiving(alist):
    fp="D:\\Summaritan\\story\\living\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1

def load4mMedia(alist):
    fp="D:\\Summaritan\\story\\media\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1


def load4mPol(alist):
    fp="D:\\Summaritan\\story\\politics\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1

def load4mWorld(alist):
    fp="D:\\Summaritan\\story\\world\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1
        
def load4mBiz(alist):
    fp="D:\\Summaritan\\story\\biz\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1


def load4mTech(alist):
    fp="D:\\Summaritan\\story\\tech\\"
    ind=0
    cnt=0
    done=False
    if len(alist)>6:
        x=6
    else:
        x=len(alist)
    while(ind<x):
        if alist[ind][1]=="" and alist[ind][2]=="":
            title, link=scrapeNR(alist[ind][0])
        else:
            title=alist[ind][1]
            link=alist[ind][2]
        if title and link !=False:
            d=buildDump(link)
            I,B=structure_story(d)
            intro=summarize(I,2)
            body=summarize(B,4)
            cnt+=1
            path=fp+str(cnt)+".html"
            f=open(path,'w+b')
            print path,"created"
            s=intro+body
            pickle.dump(s,f)
            f.close()
        ind+=1

def doNY(trend):
    Trend=  urllib.quote_plus(trend)
    data = urllib.urlopen('http://api.nytimes.com/svc/search/v1/article?format=json&query=title%3A'+Trend+'&api-key=88bd2fe67f4cb65054af624cdd974772:6:67505297').read()
    d = json.loads(data)
    if (d['total']!=0):
        x=d['results'][0]['url']
        return (x)
    else:
        return False

def doGuardian(trend):
    Trend=  urllib.quote_plus(trend)
    data = urllib.urlopen('http://content.guardianapis.com/search?q='+Trend+'&format=json&api-key=vgkc7nxahmfckz4der35bb5e').read()
    d = json.loads(data)
    print d['response']
    status = d['response']['status']
    if (status == 'ok')and d['response']['total']!=0:        
        done = "true"
        x=d['response']['results'][0]['webUrl']
        return x
    else:
        return False

def scrapeNR(trend):
    Trend=  urllib.quote_plus(trend)
    key="AIzaSyAZvy0FgL45Cd8ORlyg1w8F2j9ZVf23NL0"
    data = urllib.urlopen('https://www.googleapis.com/customsearch/v1?q='+Trend+'&key='+key+'&cx=011352445189763319440:kd1b6h_0zao').read()
    d = json.loads(data)
    if d['queries']['request'][0]['totalResults']!=0:
        result=d['items'][0]
        return result['title'], result['link']
    else:
        return False, False
        
def buildDump(link):
    print link
    my_reporter = reporter.Reporter()
    my_reporter.read(url=link)
    print my_reporter.report_news()
    return my_reporter.report_news()

def structure_story(text):
    body=[]
    intro=[]
    api_key = "oU0luKAL4u1UzqCUmWI4JXgYhs+"
    outputFormat = "json"
    sentences=split_to_sentences(text)
    for sentence in sentences:
        try:
            sentence = sentence.decode('utf-8').encode('ascii', 'ignore')
        except Exception:
            continue
        baseUrl = "http://uclassify.com/browse/zrjohn/IntroductionorBodyorConclusion/ClassifyText?"
        requestUrl = baseUrl+"readkey="+api_key+"&"+urllib.urlencode({'text':sentence})+"&version=1.01"+"&output="+outputFormat
        response = urllib.urlopen(requestUrl)
        resp=json.loads(response.read())
        cls=resp['cls1']
        cls=sorted(cls.iteritems(), key=operator.itemgetter(1), reverse=True)
        if cls[0][0]=="intro":
            intro.append(sentence)
        if cls[0][0]=="body":
            body.append(sentence)
    return "\n".join(intro), "\n".join(body)
        
    
def tokenize(text):
    return text.split()

def split_to_sentences(text):
    sentences = []
    start = 0
    
    for match in re.finditer("(\s*[.!?]\s*)|(\n{2,})", text):
        sentences.append(text[start:match.end()].strip())
        start = match.end()
        
    if start < len(text):
        sentences.append(text[start:].strip())
    return sentences

def token_frequency(text):
    '''Return frequency (count) for each token in the text'''
    frequencies = defaultdict(repeat(0).next)
    for token in tokenize(text):
        frequencies[token] += 1
    return frequencies

def sentence_score(sentence, frequencies):
    return sum((frequencies[token] for token in tokenize(sentence)))

def create_summary(sentences, max_length):
    summary = []
    senlen = 0
    for sentence in sentences:
        senlen += 1
        if senlen >= max_length:
            break
        summary.append(sentence)
    return summary

def summarize(text, max_summary_size):
    frequencies = token_frequency(text)
    sentences = split_to_sentences(text)
    sentences.sort(key=lambda s: sentence_score(s, frequencies), reverse=1)
    summary = create_summary(sentences, max_summary_size)
    summary.sort( lambda s1, s2:text.find(s1) - text.find(s2) )
    return "\n".join(summary)


extractTrends()
loadBuilder()
