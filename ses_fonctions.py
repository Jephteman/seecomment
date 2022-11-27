import requests as rq

# n'avoir que le lien de la racine
def racine(url):
	if 'https://' in url[0:8]:
		domain = 'https://'+url.split(sep='https://')[0]
	elif 'http://' in url[0:8]:
		domain = 'http://'+url.split(sep='http://')[0]
	else:
		domain = url.split(sep='/')[0]
	return domain

# Fonction pour obtenir les commentaire
def search_comment(url):
	try:
		if url is None:
			return

		request=rq.get(url)
		if 'text' in request.headers['Content-Type']:
			text=str(request.text)
		else:
			return
		links=[]
		comments=[]
		text1=text.split(sep="href=\"")
		for link in text1:
			link=link.split(sep="\"" or "\">" or "<")[0]
			if ('https://' or 'htpp://') in link[0:8]:
				pass
			else:
				link=url+link
			links.append(link)


		text2= text.split(sep="<!--")
		for comment in text2:
			comments.append(comment.split(sep='-->')[0])
		return (links , comments)
	except KeyError:
		pass



def verif(x):
	if ('https://' or 'http://') in x[0:8]:
		return True
	else:
		return 'http://'+x

def compare(url1, url2):
	return racine(url1) == racine(url2)


#print(search_comment('http://localhost/cyberchef/'))
