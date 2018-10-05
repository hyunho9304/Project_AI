import requests
from bs4 import BeautifulSoup as Soup
import re
from crawling.category import getRankURL

def getURL(category, date):
	url = getRankURL(category) + str(date)
	urlArr = []
	r = requests.get(url)
	if r.status_code == 200:
		soup = Soup(r.text, "html.parser")
		url_list = soup.find_all(class_ = 'ranking_headline')
		print(url_list)
		for i in range(20):
			urlArr.append(url_list[i].a.attrs['href'])
	return urlArr


def getNews(urlList):
	base = 'http://news.naver.com'
	p = re.compile('<[ \t\n\r\f\va-zA-Z0-9"\/\_\-\!=.?:&;#]*>')
	q = re.compile('<div.*</script>', re.DOTALL)
	q2 = re.compile('<!-.*->',re.DOTALL)
	newsArr = []
	for i in range(len(urlList)):
		temp = base + urlList[i]
		r = requests.get(temp)
		if r.status_code == 200:
			soup = Soup(r.text, 'html.parser')
			title = soup.find_all(id = 'articleTitle')
			content = soup.find_all(id = 'articleBodyContents')
			temp2 = q.sub('', str(content[0]))
			temp2 = q2.sub('', temp2)
			newsArr.append({'title' : p.sub('',str(title[0])), 'content' : p.sub('',temp2), 'url' : temp})
	return newsArr

def getSports(category, date):
	url = getRankURL(category) + str(date)
	urlArr = []
	r = requests.get(url)
	if r.status_code == 200:
		soup = Soup(r.text, "html.parser")
		url_list = soup.find_all(id = '_newsList')
		print(url_list)

		for i in range(20):
			urlArr.append(url_list[i].a.attrs['href'])
	return urlArr

