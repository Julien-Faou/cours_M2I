# Cloud computing

* Partage de risque : Contractualisation des responsabilités des parties.
=> __Le client est propriétaire des données__

* Le cloud s'engage sur la disponibilité des données, non a leurs sécurités, ils ne seront pas responsable du vol de donnée.

contractuel : 
On est en droit de négocier :
- MAJ logiciel < 24h
- PATCH des CVEs sous X jours


## Cloud privé

### Inconvénients
* Mission impossible pour une simple PME, il vaut moieux externaliser vers AWS, OHV, JAGUAR network, etc
* Très complexe, temps, formations, maintien
* Necessite une vrai culture de sécurité
* Très très cher
* Besoin de faire des exercices sur les incidents.

### Avantages
* Contrôle totale des données
* On sait qui intervient sur les données (changement disques, traitement etc)


## Cloud public

### Inconvénients
* Contractuel, bien faire attention à ce que l'on signe lors du contrat.
* Récupérer les données ? => à stipuler dans le contrat


### Avantages


## cloud partagé

### Inconvénients

### Avantages

## SAAS


## Superviseurs

### T1
* ESXI
* Hyper-V, demarre avant l'OS





## Sécurité physique:
### Hardening serveur

* bios
* chiffrements physique
* maj firmware
* hyperviseur / VMs
* gestion centralisée
* communication LAN chiffrées (Serveur -> SAN)
* Démarage impossible GRUB Monouser

### Accès physique

## Template
* Modèle sécurisé pour un type d'équipement -> Connaissance des règles de sécurités implémentées
=> Savoir les règles de par feu

## Monitoring
* Fournisseur collect suffisement de logs pour qualifier et investiguer les incidents

## Configuration des accès distants
* Maintien, sécurisation : etat de l'art du métier

## par feu
* Configurer

## IDS/IPS
* Garantissent la surveillance active/passive des flux applicatifs => droit de copie des logs vous concernant

## Honeypot : 
* Présence + monitoring

## Vulnerability assessment
1) Le data center est très claire sur sa politique de security assessment
2) Droit de X jours / ans pour pentest

## IAM - Identify Access Management
### Gestion des identités
* Depot des identités : AD / X500 / LDAP
=> Rôle ou profils rôle } templates

### Gestion des droits (applications multiples)
* Règles d'accès
* Liste des objets et le profil nécessaire pour y accéder

### SSO
__Le tout entreconnecté via SSO__

### Fédération identité
* SSO sous stéroïde
=> comme les jeux vidéos, authentification sur le jeu par google, SSO sur google qui est fédéré à l'appli.

#### OAuth
* https
* Téléphone

#### OpenID
* Fork OAuth 2
* Pas besoin de password

## WAF
* Par feu spécifique : connait le fonctionnement "normal" de l'application
* 1 WAF = 1 application
* Deep inspection

## DAM Database Activity Monitoring
* Surveiller les activités anormales de la BDD
=> bloquer les transactions
=> bloquer des selects

## REST : REpresentationnal State Transfert
* URL
* XML
* JSON

## SOAP : Simple Object Access Protocol 
* Favoriser entre echange web (https)
=> SMTP
=> HTTP
=> FTP
* Gestion des erreurs avancée
* Très strict dans le format échange


# OWASP ?
* Passer le tout dans la moulinette OWASP => faire tester
