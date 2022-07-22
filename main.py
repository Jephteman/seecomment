#/bin/python3
"""
Auteur : Jephte Man as Mr me
mail : jephte_man@protomail.com
Version : 1.0
"""
import argparse
import os
import sys
import time
import ses_fonctions as sf  # module cree pour ce programme

def start(parser):
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
		
	print(' Nous commmencons ')
	deja_visiter=[u]
	n=0
	
	
	try:
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
	except KeyboardInterrupt:
		print('bye, bye !')	
	except TypeError:
		print('Aucun resultants')
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', type=str,help='Lien vers la cible')
	
	parser.add_argument(
		'-u', default=None , help='User-agent',type=str
		)
	parser.add_argument(
		'-p',default=None,help='Destination port',type=int
	)
	parser.add_argument(
		'-v' ,default='', help='Affiche la version'
	)
	args = parser.parse_args()
	start(args)
