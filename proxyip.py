#-*-coding:utf8-*-

import re,threading,requests,time
import urllib.request
from bs4 import BeautifulSoup as BS


rawProxyList = []
checkedProxyList = []
targets = []
headers =  {
        'User-Agent': r'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Connection': 'keep-alive'
    }

for i in range(1,4):
    target = r"http://www.xicidaili.com/nn/%d" %i
    targets.append(target)
    #print (targets)

#获取代理的类
class ProxyGet(threading.Thread):
    def __init__(self,target):
        threading.Thread.__init__(self)
        self.target =target

    def getProxy(self):
        print ("目标网站："+self.target)
        r = requests.get(self.target,headers =headers)
        page = r.text
        soup = BS(page,"lxml")
        #这里的class_用的是"Searching by CSS class""，BS文档中有详细介绍
        tr_list = soup.find_all("tr", class_= "odd")
        ##ip_list > tbody > tr:nth-child(2) > td:nth-child(2)
        #//*[@id="ip_list"]/tbody/tr[2]/td[2]

        for i in range(len(tr_list)):
            row = []
            #.stripped_strings 方法返回去除前后空白的Python的string对象.
            for text in tr_list[i].stripped_strings:
                row.append(text)
            #row = ['58.208.16.141','808','江苏苏州','高匿','HTTP,......]
            ip =row[0]
            port = row[1]
            agent = row[4].lower()
            addr =agent+ "://" + ip + ":" + port
            proxy = [ip, port, agent, addr]
            rawProxyList.append(proxy)

    def run(self):
        self.getProxy()

#检验代理类
class ProxyCheck(threading.Thread):
    def __init__(self,proxyList):
        threading.Thread.__init__(self)
        self.proxyList = proxyList
        self.timeout =2
        self.testUrl = "https://www.baidu.com/"

    def checkProxy(self):

        for proxy in self.proxyList:
            proxies = {}
            if proxy[2] =="http":
                proxies['http'] = proxy[3]
            else:
                proxies['https'] = proxy[3]
            t1 =time.time()
            try:
                r = requests.get(self.testUrl, headers=headers, proxies=proxies, timeout=self.timeout)
                time_used = time.time() - t1
                if r:
                    checkedProxyList.append((proxy[0],proxy[1],proxy[2],proxy[3],time_used))
                else:
                    continue
            except Exception as e:
                continue

    def run(self):
        self.checkProxy()
        print("hello")


if __name__ =="__main__":
    getThreads = []
    checkedThreads = []

# 对每个目标网站开启一个线程负责抓取代理
for i in range(len(targets)):
    t= ProxyGet(targets[i])
    getThreads.append(t)

for i in range(len(getThreads)):
    getThreads[i].start()

for i in range(len(getThreads)):
    getThreads[i].join()

print ('.'*10+"总共抓取了%s个代理" %len(rawProxyList) +'.'*10)

#开启20个线程负责校验，将抓取到的代理分成20份，每个线程校验一份
for i in range(10):
    n =len(rawProxyList)/10
    #print (str(int(n * i))+ ":" +str(int(n * (i+1))))
    t = ProxyCheck(rawProxyList[int(n * i):int(n * (i+1))])
    checkedThreads.append(t)

for i in range(len(checkedThreads)):
    checkedThreads[i].start()

for i in range(len(checkedThreads)):
    checkedThreads[i].join()
print ('.'*10+"总共有%s个代理通过校验" %len(checkedProxyList) +'.'*10  )


#持久化
f = open("proxy_list.txt",'w+')
for checked_proxy in sorted(checkedProxyList):
    print ("checked proxy is: %s|%s" %(checked_proxy[3],checked_proxy[4])  )
    #f.write("%s:%st%st%st%s\n" % (checked_proxy[0], checked_proxy[1], checked_proxy[2], checked_proxy[3], checked_proxy[4]))
    f.write("%s|%s\n" % ( checked_proxy[3], checked_proxy[4]))
f.close()