from __future__ import unicode_literals
import cPickle as pickle
from BeautifulSoup import BeautifulSoup, SoupStrainer
import re
import httplib2


def extract_recipe(url,connection):
	status, response = http.request(url)

	soup = BeautifulSoup(response)

	mytitle = soup.findAll('h1', {"class" : "recipe-title fn"})
	mylists = soup.findAll('li', {"class" : "ingredient"})

	for title in mytitle:
		this_title = title.getText()

	ingredient_list = []

	for li in mylists:
		ingredient_list.append(li.getText().encode('utf8', 'replace'))

	return [this_title,ingredient_list]

def get_all_recipes(url_list,connection):
	ingredient_list = []
	title_list = []
	source = []

	for url in url_list:

		print "Hitting url: ", url, " ....."
		try:
			recipe = extract_recipe(url,http)
			print "Title: ", recipe[0]
			print "Ingredients: ", recipe[1]
			title_list.append(recipe[0])
			ingredient_list.append(recipe[1])
			source.append(url)

		except UnboundLocalError:
			print "Nothing to hit, moving on"

	cookbook = {}
	for i in range(len(title_list)):
		cookbook.add({title[i]: {'source' : source[i], 'ingredients' : ingredient_list[i]}})

	pickle.dump(cookbook,open("cookbook.p","wb"))

http = httplib2.Http()

url_list = pickle.load(open("updated_list.p","rb"))

get_all_recipes(url_list,http)