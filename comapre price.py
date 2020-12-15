import requests

from bs4 import BeautifulSoup

flipcart="https://www.flipkart.com/redmi-note-9-pro-champagne-gold-128-gb/p/itma84d60532d415?pid=MOBFVNYYZZ6AJT44&lid=LSTMOBFVNYYZZ6AJT44FK2QOT&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a326043d-3326-4625-ae75-768eed115f27.MOBFVNYYZZ6AJT44.SEARCH&ppt=sp&ppn=sp&ssid=s2ufbxaldc0000001607933107020&qH=8d4803676550cca6"

amazon="https://www.amazon.in/Redmi-Note-Pro-Champagne-Storage/dp/B086977J4T/ref=sr_1_1?crid=1G4ZOO3ZIXVVF&dchild=1&keywords=redmi+note+9+pro+champagne+gold%2C+128gb&qid=1607933382&s=electronics&sprefix=redmi+9+pro+gold+128%2Celectronics%2C372&sr=1-1"

netmeds="https://www.flipkart.com/redmi-note-9-pro-champagne-gold-128-gb/p/itma84d60532d415?pid=MOBFVNYYZZ6AJT44&lid=LSTMOBFVNYYZZ6AJT44FK2QOT&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=a326043d-3326-4625-ae75-768eed115f27.MOBFVNYYZZ6AJT44.SEARCH&ppt=sp&ppn=sp&ssid=s2ufbxaldc0000001607933107020&qH=8d4803676550cca6"

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

res=requests.get(flipcart).content

res1=requests.get(amazon,headers=HEADERS).text

res2=requests.get(netmeds).content

soup=BeautifulSoup(res,features="html.parser")

soup1=BeautifulSoup(res1,features="html.parser")

soup2=BeautifulSoup(res2,features="html.parser")

title=soup.find('span',class_="B_NuCI")
price=soup.find('div',class_="_30jeq3 _16Jk6d")

title1=soup1.find("span",{"id":"productTitle"})
price1=soup1.find("span",{"id":'priceblock_ourprice'})


title2=soup2.find('h1',class_="black-txt")
price2=soup2.find("span",{"id":'total_amount'})


print("Title:",title.text)
print('price available at flipkart:',price.text)

print("Title =",title1.text.strip())
print("price available at amazon =",price1.text)

print("Title:",title2.text.strip())
print('price available at netmeds:',price2.text)
