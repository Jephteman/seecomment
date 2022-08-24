# Seecomment

Seecomment est **un script offencife** permettant de lire les commentaires dans des pages HTML, et pour ce faire il procede par **fuzzing**

Seeecoment ayant trouvée un commentaire , il afffiche le lien vers la page du commentaire ensuite le commmentaire.

## Auteur

Jephte Man(Jephte Mangenda)
[Facebook]('https://facebook.com/jephteman')
[Twitter]('https://twitter.com/mr_me101)
[Tryhackme]('https://tryhackme.com/p/jephte')

Version  1.0

## Installation

Pour installer ce script , rien de plus simple que d'executé ces commandes

> git clone https://github.com/Jephteman/seecomment.git
> cd seecomment
> python3 seecoment.py http://exemple.xyz


## Usage

  python seecoment.py [options] url

  Positional arguments:
    url         Lien de la cible

  optional arguments:
    -h, --help  show this help message and exit
    -u         User-agent
    -p         Desctination port (defaut 80 ou 443)
    -v         Affiche la version

## Exemple
