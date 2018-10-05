from crawling import crawling as c
import csv
import time
import word2vec
import cluster

category = ['politics', 'economy', 'life', 'sports', 'entertainment']
now = time.localtime()
date = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
temp = category[2]


def startCrawling():
	urlList = c.getURL(temp, date)
	newsList = c.getNews(urlList)
	f = open('data.csv', 'a', encoding='utf-8', newline='')
	wr = csv.writer(f)
	for i in range(len(newsList)):
		wr.writerow([temp, newsList[i]['title'], newsList[i]['content'], newsList[i]['url'], date])
	f.close()

def sports():
	urlList = c.getSports(temp, date)
	print(urlList)


word2vec.run()
cluster.run()