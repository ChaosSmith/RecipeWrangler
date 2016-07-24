import cPickle as pickle 

url_list = pickle.load(open("complete_list.p","rb"))

updated_list = []

for url in url_list:
	if len(url) > 55 and url[27:34] == "recipes" and url[-5:] == ".html":
		print url
		updated_list.append(url)

pickle.dump(updated_list,open("updated_list.p","wb"))
