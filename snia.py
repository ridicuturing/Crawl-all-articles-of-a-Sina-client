# coding=utf-8
import requests
import bs4
import os
from bs4 import BeautifulSoup

def getPicture(url,num,root):
	try:
		f = open(root + str(num) + ".jpg",'wb')
		r = requests.get(url)
		f.write(r.content)
		f.close()
	except:
		print(url,"false")

def getArticle(url,root):
	try:
		num = 1
		f = open(root+"words.txt",'wb')
		r = requests.get(url)
		r.encoding = r.apparent_encoding
		soup = BeautifulSoup(r.text,'html5lib')
		m = soup.find(id="sina_keyword_ad_area2")
		for i in m.children:
			if isinstance(i,bs4.element.Tag):
				if(i.string):
					f.write(i.string.encode('utf-8'))
					f.write('\n'.encode('utf-8'))
				else:
					try:
						getPicture(i.find('img').attrs['real_src'],num,root)
						num = num+1
					except:
						asd=1
		f.close()
	except:
		f.close()
		print(url," false")

def makeFileFromUrl(url,name,time):
	root = "d://123//"
	path = root + time.split(' ')[0] + name
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			os.mkdir(path)
			getArticle(url,path+"//")
			print(path,"success")
	except:
			print(path,"false")
			

for q in range(2,18):
	url="http://blog.sina.com.cn/s/articlelist_1281912467_0_"+str(q)+".html"
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	soup = BeautifulSoup(r.text,'html5lib')
	m = soup.find_all('a')[23]
	papa = m.parent.parent.parent.parent
	name = []
	time = []
	url = []
	for i in papa.find_all('a'):
		if isinstance(i,bs4.element.Tag):
				if(i.string):
					name.append(i.string)
					url.append(i.attrs['href'])


	for i in soup.find_all(True,'atc_tm SG_txtc'):
		if isinstance(i,bs4.element.Tag):
			time.append(i.string)
	for i in range(1,len(name)):
		print(name[i])
		print(time[i])
		print(url[i])
		makeFileFromUrl(url[i],name[i],time[i])

