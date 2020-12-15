---
title: "FAOU_Julien_Stuxnet"
author: ["Enseignant responsable: Damien Naviliat"]
date: "2020-12-14"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Julien Faou"
titlepage: true
titlepage-color: "FF8C00"
titlepage-text-color: "FFFAFA"
titlepage-rule-color: "FFFAFA"
titlepage-rule-height: 2
listings-no-page-break: true
disable-header-and-footer: false
book: true
classoption: oneside
code-block-font-size: \footnotesize
---

![stuxnet](/OSCP-Exam-Report-Template-Markdown-master/src/images/stuxnet.png)

# Travail à réaliser

A) Résumer en une vingtaine de lignes maximum en quoi a consisté l'attaque stuxnet. (Vous passerez par ce faire par la fameuse métode QQOQCP: Quoi/Qui/Où/Quand/Comment/Pourquoi)

B) Si le site principal visé était classé SEVESO, quel serait sont classement et pourquoi?

C) De quel type de site industriel parle t'on (au sens des définitions vues dans le cours)?

D) Quels sont les niveaux du modèle purdue qui sont atteints par cette attaque?

E) Quelles sont les mesures de sécurité qui auraeint du être mises en place et ne l'on pas été? Quels sont les niveaux du modèle purdue qui auraient été mieux protégés pour chacune des mesures que vous énnoncez?

F) En complétant le contenu proposé par vos propres recherches, et en citant vos sources, la payload utilisée pour cette attaque sur les installation Iranienne s'est elle propagée sur d'autres sites? Y a t'il eu une évolution de cette attaque qui a vu le jour par la suite? 

# Réponses
## Question A
### Quoi ?

Stuxnet est le nom donné à la toute première cyberattaque ciblée. Visant les centrifugeuses des centrales nucléaires en Iran, encore inconnu aux yeux du monde, Stuxnet fit sa notoriétée en janvier 2010 avec la découverte du vers. 

Lors d'une inspection d'un site nucléaire, des inspecteurs signalent que les centrifugeuses ont un taux de casse bien trop élevé. Les techniciens ont procédés au remplacement des centrifugeuses, mais le problème persistait. 
5 mois suivèrent, lorsque lors d'un problème technique sur des ordinateurs, des intervenants ont trouvés de multiples fichiers malicieux. Ceci marque le début de la cybercriminalité avec la toute première arme digitale.

### Qui ?

Stuxnet serait une arme digitale développé par la NSA en collaboration avec l'Israel (unité 8200) visant les centrales d'Iran, notamment la centrale de Natanz

### Où ? 

La cible était une centrale nucléaire du nom de Natanz, situé en Israel

![localisation](/OSCP-Exam-Report-Template-Markdown-master/src/images/localisation.png)

### Quand ?

Stuxnet à débuter en 2007 lors du début de sa conception, l'attentat a eu lieu en 2008, mais découverte seulement en janvier 2010.

### Comment ?  

L'environement informatique de la centrale visée est isolé du rete du monde, c'est via une clé USB que la NSA, armé de son vers, a pu pénétrer dans la centrale de Natanz. Infectant les ordinateurs, puis les calculateurs siemens des centrifugeuses. Ces calculateurs servait à réguler la vitesse de rotation des centrifugeuses.

Les attaquants ne sont pas passés directement par la central de Natanz, ils ont utilisés les sous-traitants. 4 entreprises on été la cible de la NSA pour mettre toutes les chance de leurs côtés. Ces entreprises ciblées gérer chacune une partie de la centrale. Il y a eu donc plusieurs versions de stuxnet !

Ce que la NSA n'avait pas prévu c'est que le virus se répande sur internet, infectant le monde entier.

### Pourquoi ?

Stuxnet a provoqué un ralentissement du programme nucléaire iranien de presque 2 ans. Ces centrifugeuses pouvait permettre au pays de fabriquer des armes nucléaires.
En détruisant ces centrales, la NSA en empêcher l'Etat Iranien de se doter d'une tel arme.


## Question B

Les centrales nucléaires ne sont pas catégorisées par SEVESO mais par l'INB et placé sous le contrôlé de l'ASN.

Si on devrait la classée dans le classement SEVESO, elle serait "__seuil haut__" => "soumis à autorisation avec servitude d'utilité publique"

__Définition du cour :__ 

```txt
AS (Autorisation et Servitudes) : Risque technologiques élevés, qui s’approchent
ou dépassent les seuils de dangerosité ou de rejet autorisés par l’état. Les seuils
dépassés sont autorisés parce que le site de production est considéré d’utilité
publique. Dans ce cas, il sera impossible d’installer d’autres sites industriels ou
habitations personnelles à proximité,
S’il y a déjà des habitations à côté d’un site SEVESO qui dépasse les normes
alors l’état qualifie l’industrie d’utilité publique et « on fait avec ».
```

![seveso](/OSCP-Exam-Report-Template-Markdown-master/src/images/seveso.jpg)

## Question C

La centrale de Natanz est un site fixe monolithique.

## Question D

Voici les niveaux du modèle CIM89 qui sont touchés par cette attaque : 

* Level 5 - Internet DMZ
* Level 4 - Enterprise
* Level 3 - Control center / Processing LAN
* Level 2 - Local HMI LAN
* Level 1 - Controller LAN

## Question E

* Désactivation de tout port USB et pas d'ordinateur personnel. - __Level 4 / 3__
* Autoriser uniquement les équipements fournits par la centrale
* Limiter les accès des prestataires, en choisir avec des normes de sécurités.

## Question F

Le payload à fuité sur internet, infectant ainsi bien plus que la centrale de Natanz en Iran. Le vers s'est propagés jusqu'à son origine aux Etats unis, le retour de bâton.

On peut retrouver des versions décompiler du vers : 

* https://github.com/micrictor/stuxnet

Depuis, les systèmes de défenses (anti-virus / IDS / SO / etc) reconnaissent et bloquent de vers.

* https://nmap.org/nsedoc/scripts/stuxnet-detect.html

# Sources

* __(WIRED)__ https://www.wired.com/2014/11/countdown-to-zero-day-stuxnet/

* __(OBS)__ https://www.nouvelobs.com/rue89/rue89-internet/20120604.RUE0433/stuxnet-comment-les-etats-unis-et-israel-ont-pirate-le-nucleaire-iranien.html

* __(SFEN)__ https://www.sfen.org/rgn/seveso-protections-centrales

* __(KASPERSKY)__ https://www.kaspersky.fr/blog/stuxnet-les-origines/3939/

