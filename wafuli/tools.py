#coding:utf-8
from django.conf import settings
import time,os
def createUrl():
    tstr = time.strftime('%Y/%m/%d/')
    html_name = str(int(time.time()))+'.html'
    directory = os.path.join(settings.MEDIA_ROOT, 'html',  tstr).replace('\\','/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, html_name), 'w') as html_file:
        pass
    url = os.path.join(settings.MEDIA_URL,'html', tstr, html_name).replace('\\','/')
    print 'url',url
    return url
def writeHtml(html,url):
    s = len(settings.MEDIA_URL)
    if url==None or len(url)<=s:
        return -1
    url = url[s:]
    url = os.path.join(settings.MEDIA_ROOT,url).replace('\\','/')
    if not os.path.exists(url):
        return -1
    with open(url, 'w') as html_file:
        html = html.encode('utf-8')        
        html_file.write(html)
    return 0
