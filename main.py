#!/usr/bin/python3

from requests_html import HTMLSession
# import json


session = HTMLSession()

url = 'https://www.annapurnapost.com/search/news?query=nepal'

r = session.get(url)

r.html.render(sleep=1,scrolldown=5)

articles = r.html.find('div')

newslist = []

for item in articles:
	try:
		newsitem = item.find('h3', first=True)
		newsarticle = {
		'title' : newsitem.text,
		'link' : newsitem.absolute_links
		}
		newslist.append(newsarticle)
		# print(title, link)
	except:
		pass

print(newslist)

# # with open('data.json','w') as outfile:
# # 	json.dump(newslist,outfile)