#/bin/python3

import argparse
import os
import ses_fonctions as sf  # module cree pour ce programme

version='1.1'

def start(parser):
	expression=' '
	u=parser.url
	cible=sf.racine(parser.url)
	if sf.verif(parser.url) != True:
		cible=sf.verif(parser.url)

	if type(parser.u) != type(None):
		def f():
			return parser.u
		sf.rq.utils.default_user_agent=f

	if type(parser.p) != type(None):
		if cible[0:8] == 'https://':
			sf.rq.utils.DEFAULT_PORTS['https']=parser.p
		elif cible[0:7] == 'http://':
			sf.rq.utils.DEFAULT_PORTS['http']=parser.p
		else:
			raise Exception('Protocole non pris en charge :{}'.format(cible))

	if type(parser.e) != type(None):
		expression=parser.e.split(sep=',')
		sf.expression=expression
	else:
		expression=' '

	print(' Nous commmencons ')
	deja_visiter=[u]
	n=0

	try:
		if type(parser.w) == type(None):
			trouver=sf.search_links(u)
			while len(trouver) != 0:
				if sf.compare(str(cible),str(sf.racine(trouver[0]))) is True:
					if trouver[0] not in deja_visiter:

						x=sf.search_links(trouver[0])
						deja_visiter.append(trouver[0])
						n+=1
						del trouver[0]
						try:
							for y in x :
								if y not in trouver and y not in deja_visiter:
									trouver.append(y)
						except:
							pass
					else:
						deja_visiter.append(trouver[0])
						del trouver[0]
				else:
					del trouver[0]
		else:

			try:
				wordlist=open(parser.w,'r')
			except:
				print('[+] Nous n\'avons pas eu acces a la wordlist')
				exit(1)

			if url[-1] != '/':
				url+='/'

			wordlist=wordlist.readlines()
			for i in wordlist:
				if i[0] == "#":
					pass
				elif i =='\n':
					pass
				else:
					comments=sf.search_comment(request.get(url+i).text)
					if comments.__sizeof__() != 40:
						for exp in expression:
							if exp in comments:
								for comment in comments:
									print('---- {} ----'.format(url+i))
									print(commet)
								break


	except KeyboardInterrupt:
		print('bye, bye !')
	except TypeError:
		print('Aucun resultants')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'url', type=str,help='Lien vers la cible'
		)
	parser.add_argument(
		'-w',type=str,help='Wordlist'
	)

	parser.add_argument(
		'-u', default=None , help='User-agent',type=str
		)
	parser.add_argument(
		'-p',default=None,help='Port',type=int
		)
	parser.add_argument(
		'-e',default=None,type=str,help='expression rechercher dans le commentaire'
		)
	args = parser.parse_args()
	start(args)
