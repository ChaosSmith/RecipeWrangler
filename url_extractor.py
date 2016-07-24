from BeautifulSoup import BeautifulSoup, SoupStrainer
import re
import httplib2
import cPickle as pickle

def extract_urls(url,connection,url_list,complete_list):

	status, response = http.request(url)

	soup = BeautifulSoup(response)

	mylinks = soup.findAll('a', href=True)

	new_urls = []

	for link in mylinks:

		if link['href'] not in complete_list and link['href'] not in url_list and link['href'] not in new_urls and link['href'][0:26] == "http://www.seriouseats.com":

			new_urls.append(link['href'])

	return new_urls

def url_crawler(start_url, connection):
	
	url_list = [start_url]
	complete_list = []

	while len(url_list) != 0:

		try:
			url_list.extend(extract_urls(url_list[0],connection,url_list,complete_list))
		except UnicodeEncodeError:
			print "There was a problem with", url_list[0]

		complete_list.append(url_list[0])
		print url_list.pop(0)


	pickle.dump(complete_list, open("complete_list.p", "wb"))


http = httplib2.Http()
url = "http://www.seriouseats.com/"

url_crawler(url,http)
