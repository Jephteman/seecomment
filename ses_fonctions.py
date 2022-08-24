import requests as rq
import requests
import socket
expression=' '

# n'avoir que le lien de la racine
def racine(url):
	url=url.split(sep='/')
	url=url[0]+'//'+url[2]+'/'
	return url

#recherche les commentaires dans les fichiers html
def search_comment(text):
	comment=[]
	i=0
	x=True
	while x:
		try:
			if text[i:i+1] == '<':

				i+=1
				if text[i:i+1] == '!':
					i+=1
					if text[i:i+1] == '-':
						i+=1
						if text[i:i+1] == '-':
							i+=1
							boucle2=True
							temp_tewt=''
							while boucle2:
								if text[i:i+1] == '-':
									i+=1
									if text[i:i+1] == '-':
										i+=1
										if text[i:i+1] == '>':
											i+=1
											comment.append(temp_text)
											temp_text=''
											break
										temp_text+=text[i-1:i]
									temp_text+=text[i-1:i]
								temp_text+=text[i-1:i]
								i+=1

			elif text[i:i+1] == '/':
				i+=1
				if text[i:i+1] == '*':
					i+=1
					boucle2=True
					temp_text=''
					while boucle2:
						if text[i:i+1] == '*':
							i+=1
							if text[i:i+1] == '/':
								i+=1
								comment.append(temp_text)
								temp_text=''
								break
							temp_text+=text[i-1:i]
						temp_text+=text[i-1:i]
						i+=1

				elif text[i:i+1] == '/' and text[i-2:i-1] != ':':
					i+=1
					temp_text=''
					while text[i:i+1] != '\n':
						temp_text+=text[i:i+1]
						i+=1
					comment.append(temp_text)
					temp_text=''

			i+=1
			if len(text) <= i:
				return comment
				break
		except KeyboardInterrupt:
			pass

#fonction  obtenir les liens
def search_links(url):
	try:
		x=rq.get(url)
		if 'text' in x.headers['Content-Type']:
			text=str(x.text)
			b=True
		else:
			return [url]
		i=0
		links=[]
		while b == True:
			i+=1
			if text[i] == 'h':
				i+=1
				if text[i] == 'r':
					i+=1
					if text[i] == 'e':
						i+=1
						if text[i] == 'f':
							i+=1
							if text[i] == '=':
								i+=1
								if text[i] == '\'' or text[i] == '\"' or text[i] == '\t' or text[i] == '\n':
									i+=1
								boucle2=True
								m=''
								while boucle2:
									m+=text[i]
									if text[i] == '\'' or text[i] == '\"' :
										if m[0:7] != 'http://' or m[0:8] != 'https://':
											if url[len(url)-1:len(url)] != '/':
												url+='/'
												pass

										links.append(m[0:-1])
										m=''
										boucle2=False
									i+=1
	except:
		try:
			c=search_comment(text)
			if c.__sizeof__() != 40:
				for i in expression:
					if i in c:
						print('n\ ',+url)
						for n in c:
							print(n)
						break

			links_ok=[x for x in links if x[0:7] == 'http://' or x[0:8] == 'https://' ]
			links_no=[racine(url)+x for x in links if (x[0:7] != 'http://' or x[0:8] != 'https://') and x not in links_ok]
			links=links_ok+links_no
			return links
		except KeyboardInterrupt:
			pass

def verif(x):
	if 'https://' in x[0:8] or 'http://' in x[0:8]:
		return True
	else:
		return 'http://'+x

def compare(url,durl):
	def dec(x):
		x=x.split(sep='/')
		return x[2]

	if dec(url) == dec(durl):
		return True
	return False
