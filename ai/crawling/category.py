url = {
	'politics' : 'http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=',
	'economy' : 'http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=101&date=',
	'life' : 'http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=',
	'sports' : 'https://sports.news.naver.com/ranking/index.nhn?date=',
	'entertainment' : 'http://entertain.naver.com/ranking#type=hit_total&date='
}

def getRankURL(category):
	return url[category]