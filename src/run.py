from crawling import crawling as c
import csv

category = ['politics', 'economy', 'life', 'sports', 'entertainment']

date = '20180604'
temp = category[3]


def run():
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
#run()
sports()