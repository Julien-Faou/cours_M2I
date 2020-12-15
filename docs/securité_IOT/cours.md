## Cloud computing

### Definition

__Définition du NIST :__

- Modèle omniprésent
- Adapté aux besoins
- Disponible à la demande
- Utilise des réseaux
    - Accéder à des moyens informatiques, partagés, configurable
- Les moyens informatique peuvent être réservés et libérés en fonction des besoins
    - __AVEC__ un effort minimal de configuration

### Facturation

__Télémétrie__, le prix est calculé sur beaucoup d'aspect : 

- Utilisation CPU
- Stockage
- etc


### Raison pour aller dans le cloud ? 

#### Economique
Pour toutes les entreprises, le service info est un centre de coût, pas de profit. 
Mais le cloud est piegeux, les coûts grimpent vite ! Mais alors au top niveau infra

#### Securité
Les informaticiens ne sont pas toujours amis avec la sécurité, maîtrise pas toujours le concept, les outils, etc...
Entre attaquer une infra d'un PME ou AWS/OVH/etc c'est pas pareil.

#### Migrer dans le cloud

1) Recencer tous les processus de l'entreprise => BPL (graph simple et comprehensible par lambda)

2) Recencer tous les biens (assessments, les choses achetées)(materiel / immateriel)

3) Recencer tous les besoins (de quoi l'entreprise a besoin)


a) échanger avec les cadres (ton service utilise quoi ? les besoins ?)
b) échanger avec les salariés (pas la même vision que les cadres)
c) échanger avec les clients (temps de paiements, comment ça se passe avec l'entreprise ?)
d) Volumétrie moyenne du réseau => séparer les flux
e) Inventaire logiciel / materiel
f) Inventaire des données compatbles
g) Inventaire des assurances (voir si les contrats sont toujours valides avec le cloud)
h) Les données personnelles (RGPD) c'est le cadre qui encadre le service qu'il gère qui gère les données personnelles des employés.
i) Analyser l'impact juridique.

#### BIA

__Business Impact Analysis__ : Etude de l'impact sur la productivité de l'entreprise si un processus métier ou un équipement/bien sur lequel repose le processus venait à faillir.

=> Etablir les chemins critiques : les processus que l'on ne pourra pas interrompre.

=> Evaluer l'impact économique en cas de rupture du process. (la hotline on s'en fou peut etre pas mal)

=> Coût de mise en conformité

#### Coût

- Réduction de la masse salariale.
- Réduction coût opérations.
- Réduction des coûts de mise en conformité.



#### Modèle économique : 

- SaaS : Sofware as a Service : emails, CRM, soft tout prêt clé en main.
- IaaS : Infrastructure as a Service : serveur baremetal
    + POSITIFS : 
        + Garde la main sur la sécurité.
        + Très utilisé pour la sauvegarde de donnée.
        + PRA / PCA (plan de secours, plan de restauration).
        + Très forte disponibilité.

    - NEGATIFS : 
        - administration
        - mises à jour
        - gain cloud minime

- PaaS : Platform as a Service : système exploitation tout prêt (instance)
    IaaS + install les mises à jour des OS
    + POSITIFS :
        + devops
    - NEGATIFS :
        - manque de visibilité sur l'hardening
        - difficulté à modifier paramètre bloqués


#### Mode de déployement : 

- Cloud partagé : équipement possédés par le fournisseur
    - Partagé entre tous les clients
- Cloud privé : L'infrastructure d'une enteprise
    - Réseau dédié
    - Serivces accessible depuis l'exterieur de l'entreprise (VPN, DMZ, frontal, etc)
    - Ne sert qu'à l'enterprise
    - /!\ Pas forcement dans les locaux /!\
- Cloud communautaire : Entreprise se regroupant pour former un cloud commun
    - Souvent des associations
    - owncloud / nextcloud
- Modèle hybride : mix 2 type de cloud

#### Type de datacenter

T1 :
- alimentation electrique secours pour serveur/sauvegarde => onduleurs
- Coupure plus longue : générateur tenant jusqu'à 12h
- Système spécifique de refroidissement des systèmes critique.
- Espace dédié aux serveur
- Espace dédié au réseau

T2 : (T1 amélioré)
- Redondance des serveurs et réseaux
- Erreurs de manipulation : l'arrêt du service n'est pas systématique
- En cas de maintenance planifiée : pas de coupure de service

T3 : (T2 amélioré)
- Tous les équipements électroniques ont un système d'alim électrique redondante.
- Les opérations essentielles continuent en cas de panne d'un composant.

T4 : la crême de la crême
- __Tout__ est redondant (fil électrique, reseau, ordi, etc)
La panne d'un système n'a pas de conséquence sur les services.
Les évolutions techniques ne causent pas d'arrêt technique.

#### Quelques outils Netflix pour foutre le bordel

* Chaos Monkey
* Doctor Monkey
* Lattency Monkey
=> Simian Army

#### Les types de biens

* Materiel
* Immateriel
* Processus
* Chemin critique
* Salariés

#### Processus

Dans tous service, peut y avoir des processsus critiques.
SPOF => single Point Of Faillure, viendra principalement du matériel ou des employés

### Frontière du cloud

Dans un cloud public, les responsabilités sont réparties entre le client et le cloud. Il existe une zone grise dans laquelle on ne sait pas trop qui est responsable : 




### Négociations

* Négocier avec le fournisseur, comment etre sûr qu'un employé n'ira pas brancher un keylogger ? Exiger les mises à jour des CVEs critiques.
* Chiffrement de disques durs.

### DLP

Data Lost Prevention, système de sauvegarde, prévention de la fuite de donnée. Va alerter si un utilisateur exfiltre des données (IA).
Il y a une phase d'apprentissage, se base sur l'usage moyen d'un utilisateur sur un soft.

#### Cycle de vie d'une donnée

1) Création de la donnée (mémoire vive, HDD, variable)(elle peut ne pas être encore stockée)

2) Utilisation de la donnée

3) Stockage

4) Partage

5) Archivage (durée de vie, à un moment cette donnée devient moins utile voir plus du tout environ 5 ans)

6) Destruction

