#coding:utf-8
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import time
import datetime
import MySQLdb
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  

def hello(request):
    return HttpResponse("<h1>Hello world!</h1>")

def mytime(request):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    t = get_template('time.html')
    c = Context({"time":now})
    return HttpResponse(t.render(c))
def gettime(request):
    mytime = time.strftime("%Y-%m-%d %H:%M:%S")
    print "locals",locals()
    return render_to_response('time.html',locals())
def changetime(request,offset):
    try:
	offset=int(offset)
    except ValueError:
	raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def bloglist(request):
    db = MySQLdb.connect(user='root',db='blog',passwd='123456',host='localhost',charset="utf8")
    cursor = db.cursor()
    cursor.execute("select * from entries")
    alldata = cursor.fetchall()
    cursor.close()
    db.close()
    print type(alldata)
    print alldata
    return  render_to_response('bloglist.html',{"list":alldata})
#if __name__=="__main__":
#    bloglist()
	
