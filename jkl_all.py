import  requests
from lxml import etree
import re
import os
url="https://www.jkl.com.cn/newsList.aspx?TypeId=10009"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers).text
html = etree.HTML(response)
pro_name=html.xpath('//div[@class="infoLis"]//a/text()')
#print(pro_name)
pro_link=html.xpath("//div[@class='infoLis']//@href")
#print(pro_link)
name=[i.strip() for i  in pro_name]
link=["https://www.jkl.com.cn/"+i for i in pro_link]
#print(name)
#print(link)
dict_all=dict(zip(name,link))
#print(dict_all)
for key,value in dict_all.items():
   key=key.replace("/",".")#将/替换成.
   key=key.replace("...","报表")
   path='D:/jkl_post/'+key
   if not os.path.exists(path):
       os.mkdir(path)
   response=requests.get(value,headers=headers).text
   html=etree.HTML(response)
   end_page=html.xpath('//a[text()="尾页"]/@href')
   if end_page!=[]:
       regex=re.search(r'current=(\d+)',end_page[0])
       page=regex.group(1)
   else:
       page=1
   #print(page)
   for i in range(1,int(page)+1):
       data={
           "__EVENTTARGET":"AspNetPager1",
           "__EVENTARGUMENT":i
       }
       response=requests.post(value,headers=headers,params=data).text
       html=etree.HTML(response)
       title=html.xpath('//div[@class="newsLis"]//li/a/text()')
       link=html.xpath('//div[@class="newsLis"]//li//@href')
       title=[i.strip() for i in title]
       if all(link):#判断列表的元素是否都不为空
           link=["https://www.jkl.com.cn/"+i for i in link]
           dict_news=dict(zip(title,link))
           for key,value in dict_news.items():
               key=key.replace("/",".")#将/替换成.
               key=key.replace("...","报表")
               response=requests.get(value,headers=headers).content
               houzhui=value.split(".")[-1]
               a_path=path+'/'+key+'.'+houzhui
              # print(path)
               with open(a_path,'wb') as f:
                   f.write(response)
                   print(key+'下载完成')
