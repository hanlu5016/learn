import requests
from bs4 import BeautifulSoup as BS


rawProxyList = []
checkedProxyList = []
targets = []
headers =  {
        'User-Agent': r'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Connection': 'keep-alive'
    }


def getProxy(target):
    print("目标网站：" + target)
    r = requests.get(target, headers=headers)
    page = r.text
    soup = BS(page, "lxml")
    # 这里的class_用的是"Searching by CSS class""，BS文档中有详细介绍
    tr_list = soup.find_all("tr", class_="odd")
    ##ip_list > tbody > tr:nth-child(2) > td:nth-child(2)
    # //*[@id="ip_list"]/tbody/tr[2]/td[2]
    # print(tr_list)
    print(len(tr_list))
    for i in range(len(tr_list)):

        row = []
        # .stripped_strings 方法返回去除前后空白的Python的string对象.
        for text in tr_list[i].stripped_strings:
            row.append(text)

        # row = ['58.208.16.141','808','江苏苏州','高匿','HTTP,......]

        ip = row[0]
        port = row[1]
        agent = row[4].lower()
        addr = agent + "://" + ip + ":" + port
        proxy = [ip, port, agent, addr]
        print(proxy)
        rawProxyList.append(proxy)

target="http://www.xicidaili.com/nn/"
getProxy(target)