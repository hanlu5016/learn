import requests
# req=requests.get(url='http://www.itwhy.org')
# print(req.status_code)
# req=requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})
# print(req.status_code)
# print(req.url)
# print(req.text)
# r=requests.get('https://github.com/')
# print(r.text)
# r2=requests.post('http://httpbin.org/post')
# print(r2.text)
# r3 = requests.put("http://httpbin.org/put")
# r4 = requests.delete("http://httpbin.org/delete")
# r5 = requests.head("http://httpbin.org/get")
# r6 = requests.options("http://httpbin.org/get")
# print(r3.text)
# print(r4.text)
# print(r5)
# print(r6)
#
# URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
#try:
#    r = requests.get(URL, params={'ip': '183.204.140.162'}, timeout=1)
#    r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常

#except requests.RequestException as e:
#    print(e)
#else:
#    result = r.json()
    #print(type(result), result, sep='\n')


#r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))

#print(r)

 
# r = requests.get('http://www.baidu.com')
#print(r.cookies['BDORZ'])
#print(tuple(r.cookies))

#如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求:
import random
f=open('proxy_list.txt','r')
# lin=len(f.readlines())
# print(lin)
proxy_list=list()
for i in f.readlines():
  #print(i)
  proxy_list.append(i.split('|')[0])
print(len(proxy_list))
# for i in proxy_list:
#   print(i.split('|')[0])

#print(random.choice(proxy_list))
# proxies = {
#   "http": "http://61.160.254.23:23",
#   "https": "http://10.10.1.10:1080",
# }
#
t=random.choice(proxy_list)
proxies = {
  "http": t,
}
r=requests.get("http://example.org", proxies=proxies)
print(r.json())

