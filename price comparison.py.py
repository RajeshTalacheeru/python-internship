#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#price comparison


# In[2]:


import requests

from bs4 import BeautifulSoup

flipcart="https://www.flipkart.com/fair-lovely-advanced-multi-vitamin-fairness-cream/p/itmeyeh7sfncwbun?pid=FRNEZ797AESFCUN2&lid=LSTFRNEZ797AESFCUN2SLR1RX&marketplace=GROCERY&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_ps&fm=SEARCH&iid=7b0485bb-cc11-468b-a9a8-bebf14e650a2.FRNEZ797AESFCUN2.SEARCH&ppt=sp&ppn=sp&ssid=afoz3wncmo0000001607789178235&qH=f0d3ad8cdea78804"

amazon="https://www.amazon.in/Fair-Lovely-Advanced-Multi-Vitamin/dp/B01CGEPVYW/ref=sr_1_2?crid=CHUH44TE6SCC&dchild=1&fpw=pantry&keywords=fair+lovely+cream&qid=1607837012&s=pantry&sprefix=fair%2Caps%2C500&sr=8-2"

netmeds="https://www.netmeds.com/non-prescriptions/fair-lovely-advanced-multi-vitamin-face-cream-50-gm?source_attribution=ADW-CPC-Shoppingads&utm_source=ADW-CPC-Shoppingads&utm_medium=CPC&utm_campaign=ADW-CPC-Shoppingads&gclid=Cj0KCQiA8dH-BRD_ARIsAC24umbcUFpljqYZtihhMPrkJSLd5i6Xv7Qwwu9UiqHi6jB9Q7fruXcoFwMaAuyqEALw_wcB"

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

res=requests.get(flipcart).content

res1=requests.get(amazon,headers=HEADERS).text

res2=requests.get(netmeds).content

soup=BeautifulSoup(res,"lxml")

soup1=BeautifulSoup(res1,"html")

soup2=BeautifulSoup(res2,"lxml")

title=soup.find('span',class_="B_NuCI")
price=soup.find('div',class_="_30jeq3 _16Jk6d")

title1=soup1.find("span",{"id":'productTitle'})
price1=soup1.find("span",{"id":'priceblock_ourprice'})


title2=soup2.find('h1',class_="black-txt")
price2=soup2.find("span",{"id":'total_amount'})


print("Title:",title.text)
print('price available at flipkart:',price.text)

print("Title =",title1.text.strip())
print("price available at amazon =",price1.text)

print("Title:",title2.text.strip())
print('price available at netmeds:',price2.text)


# In[ ]:




