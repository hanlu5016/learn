import urllib.request
import time
from bs4 import BeautifulSoup
import re
import random

import time

def get_html(url,head):
    webheader1 = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'}
    #wb_data=requests.get(url,headers =webheader1)
    request = urllib.request.Request(url,headers = webheader1)
    response = urllib.request.urlopen(request)
    html =response.read().decode("gbk")
    time.sleep(random.randint(0,10))
    #print(html)

    try:
        split_head=head.split('/')
        fileName=split_head[1]+'_'+split_head[3]

        f_obj=open('d:/work/cl/'+fileName,'w')
        f_obj.write(html)

    except Exception as ex:
        print(ex)

    print(head)



def get_page(url):
    webheader1 = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'}
    #wb_data=requests.get(url,headers =webheader1)
    request = urllib.request.Request(url,headers = webheader1)
    response = urllib.request.urlopen(request)
    html =response.read().decode("gbk")
    c_re=re.compile('<input type="text" style="width:50px;" value=\"1\/(.+?)\"')
    #print(html)
    page=c_re.findall(html)[0]
    return page













def get_list(url,ll):
    webheader1 = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'}
    #wb_data=requests.get(url,headers =webheader1)
    request = urllib.request.Request(url,headers = webheader1)
    response = urllib.request.urlopen(request)
    html =response.read().decode("gbk")
    time.sleep(3)
    #print(html)
    #print(ll.findall(html)[0])

    soup=BeautifulSoup(html,'lxml')
    t_hs=soup.select(ll)
    #t_hs=soup.find_all("a",class_="s xst")
    #print(t_hs)
    s="http://m.vvznin.com/"
    ti=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    for t_h in t_hs:
        he=t_h.get('href')
        h = s + he
        t = t_h.get_text()
        print("Title:%s|web:%s" % (t, h))
        get_html(h,he)
        
 
        try:
            f_log = open('cl_log.txt', 'a')
            f_log.write(ti+t + '|' + h + '\n')
        except Exception as ex:
            print(ex)

    #print(soup.select(url_id))


url_jishu="http://m.vvznin.com/thread0806.php?fid=7&search=&page=1"
url_id=re.compile('<input type="text" style="width:50px;" value=\"1\/(.+?)\"')
l_r="# h3 > a"

#get_list(url_jishu,l_r)
#get_list(url_jishu,url_id)
#get_html(url_jishu,'jishu.html')
#print(get_page(url_jishu))
#get_html(url_jishu,'leas')

for i in [7,16,2,22,20,15,8,5,4,21]:
    url="http://m.vvznin.com/thread0806.php?fid="+str(i)+"&search=&page=1"
    t=get_page(url)
    m=int(t)+1
    for x in range(m):
        url_list="http://m.vvznin.com/thread0806.php?fid="+str(i)+"&search=&page="+str(x)
        try:
            get_list(url_list, l_r)
        except Exception as ex:
            print(ex)


