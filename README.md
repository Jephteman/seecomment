# seecomment
ce programme facilite la tâche d'un penetesteur ou d'un jouer de CTF en ce qui concerne la lecture de collentaire dans les pages html

#Usage
                                                                  
┌──(root💀localhost)-[/home/jephte/git_down/seecomment]
└─# python main.py -h
usage: main.py [-h] [-u U] [-p P] [-v V] url

positional arguments:
  url         Lien vers la cible

options:
  -h, --help  show this help message and exit
  -u U        User-agent
  -p P        Destination port
  -v V        Affiche la version

#Exemple
──(jephte㉿localhost)-[~/git_down/seecomment]
└─$ python main.py http://localhost/wordpress
 Nous commmencons 

 --- http://localhost/wordpress/ ---
s.w.org' />
*! This file is auto-generated
 Early exit if a skip-link target can't be located.
 Get the site wrapper.
 The skip-link will be injected in the beginning of it.
 Early exit if the root element was not found.
 Get the skip-link target's ID, and generate one if it doesn't exist.
 Create the skip link.
 Inject the skip link.

 --- http://localhost/wordpress/wp-content/themes/twentytwentytwo/style.css?ver=1.0 ---

