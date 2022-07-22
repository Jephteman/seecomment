import requests as rq
import requests
import socket

# n'avoir que le lien de la racine
def racine(url):
	i=0;x=''
	n=0
	try:
		while i != 3:
			x+=url[n]
			if x[n] == '/':
				i+=1
			n+=1
			if i == 3:
				return x
	except:
		return x

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
	except IndexError:
		try:
			c=search_comment(text)
			if c.__sizeof__() > 40:
				print('\n --- '+url+' ---')
				for n in c:
					print(n)
			
			links_ok=[x for x in links if x[0:7] == 'http://' or x[0:8] == 'https://' ]
			links_no=[racine(url)+x for x in links if (x[0:7] != 'http://' or x[0:8] != 'https://') and x not in links_ok]	
			links=links_ok+links_no
			return links
		except KeyboardInterrupt:
			pass
	except requests.exceptions.ConnectionError:
		try:
			c=search_comment(text)
			if c.__sizeof__() != 16:
				print('n\ ',+url)
				for n in c:
					print(n)
			
			links_ok=[x for x in links if x[0:7] == 'http://' or x[0:8] == 'https://' ]
			links_no=[racine(url)+x for x in links if (x[0:7] != 'http://' or x[0:8] != 'https://') and x not in links_ok]
			links=links_ok+links_no
			return links
		except KeyboardInterrupt:
			pass		

# compare deux noms des domaines s'ils sont du meme reseaux
def verif(x):
	if 'https://' in x[0:8] or 'http://' in x[0:8]:
		return True
	else:
		return 'http://'+x

def compare(url,durl):
	def dec(x):
		c=0
		n=0
		for i in x:
			if i == '/':
				n+=1
			if n == 2:
				break
			c+=1
		x=x[c:len(x)]
		if x[len(x)-1:len(x)] == '/':
			return x[1:len(x)-1]
		else:
			return x[1:len(x)]
	
	if dec(url) == dec(durl):
		return True
	elif durl[len(dec(durl))-len(dec(url)):len(dec(durl))] == dec(url):
		return True
	else:
		#print(durl+ '   comp')
		return False 

"""	
n=open('test.txt','r')
n=str(n.read())

print(search_comment(n))
"""