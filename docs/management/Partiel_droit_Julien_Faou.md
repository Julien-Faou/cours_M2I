---
title: "Partiel droit"
author: ["Julien Faou"]
date: "2020-11-20"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "M2I 2018"
lang: "en"
titlepage: true
titlepage-color: "FF8C00"
titlepage-text-color: "FFFAFA"
titlepage-rule-color: "FFFAFA"
titlepage-rule-height: 2
listings-no-page-break: true
disable-header-and-footer: false
book: true
classoption: oneside
code-block-font-size: \scriptsize
---

# A - Mise en pratique des règles relatives à la force majeure

## Principe de force majeure : 

Les cas de forces majeures sont définis comme des situations à la fois : 
* __irréssistibles / insurmontable__ :  Une situation dont on ne peut pas faire autrement
* __imprévisibles__ : Une situation que l'on n'avait pas prévu. Un problème technique dans les locaux en week end.
* __indépendantes des parties__ : Qui n'est lié en aucun cas aux deux parties, hors de leurs contrôles.

__Une catastrophe naturelle, un événement climatique exceptionnel sont des cas de force majeure, si ces situations imprévisibles échappent au contrôle des personnes et sont par nature inévitables. Le décès du salarié constitue pour le contrat de travail un cas de rupture pour force majeure. Le verglas et les chutes de neige sont en hiver des événements prévisibles qui ne constituent pas des cas de force majeure. En cas de litige, ce sont les tribunaux qui décident si l'événement relève de la force majeure.__
 
Source : https://www.service-public.fr/particuliers/vosdroits/F33790

## Les clauses de la SSI pour les cas de force majeure :

Cette étude cible le SI du secteur de l'énergie :
Les SI des secteurs de l'énergie gèrent des données sensibles, ils permettent de piloter la distribution, la production ainsi que l’acheminement de l'électricité auprès des particuliers, entreprises, gouvernement, etc.
l’ANSSI ainsi que les gouvernements place ce secteurs d’activité dans la catégorie des OIV (Opérateur d’Importance Vitale). Ces secteurs sont soumis à la LPM (Loi de Programmation Militaire). De ces fortes contraintes en matière de Sécurité du Système d’Information, les prestataires doivent être accrédité Secret Défense et être accrédité par la LPM.

Nous avons défini plusieurs clauses spécifique à ajouter à un contrat de prestation :

* __SSI du client :__ Les directives Européennes imposent aux RSSI ainsi qu'aux prestataires une responsabilité de résultat pour garantir la sécurité de celui-ci. Je pense que cette responsabilité de résultat doit être rétrogradée en responsabilité de moyens. La cour de cassation de la troisième chambre civile a rendu un arrêté qui caractérise un bogue informatique comme un cas de force majeure. https://www.legifrance.gouv.fr/juri/id/JURITEXT000021855151/ De ce constat, il me semble impossible de garantir une responsabilité de résultat à la totalité des prestataires. Il me semble donc nécessaire de l’intégrer au contrat de prestation de mes clients.

* __SSI du prestataire :__ Je pense que le prestataire doit ajouter une clause dans ses contrats de prestations spécifiant que le client ne peut pas se retourner contre le prestataire de service si son Système d’Information devient la cible d’une attaque. Ce qui pourrait donner suite à une fuite des données à caractères confidentiel, secret défense ainsi que confidentiel défense. Cette clause doit donc protéger la responsabilité du prestataire pour garantir la sécurité juridique de ses salariés et de l’entreprise.	L'entreprise Sopra Steria a été victime d’une attaque informatique le 20 octobre. Pour conclure ce point je pense que les prestataire doivent spécifier une garantie de moyen sur la protection de leurs SI et des données clients.

* __La sauvegarde des données du SI :__ Le prestataire ne doit pas être tenu responsable en cas de défaillance logique ou physique. Qui peuvent être lié à l’activité humaine ou industrielle des clients ou de différents prestataires qui viendrait à intervenir sur les équipements.

* Je pense qu’il faut spécifier avec clarté dans le contrat après s’être justifié par le biais des paragraphes précédents, que le prestataire ne pourra pas être tenu pour  responsable en cas d’attaque informatique sur le système. Malgré que les différents collaborateurs du prestataire suivent une veille active et des formations sur différentes thématique de la Sécurité des Systèmes d’Information.

* Le prestataire ne doit pas être tenu responsable d’inactivité en cas de risque physique (catastrophes naturelles, événement climatique exceptionnel, attaque terroriste, guerre, ect...)  ou sanitaire (pandémie). 


# B - Les finalités en matières de données à caractères personnelles :

## Engie
| Finalité              | Type de collecte/controle | Nature de la mesure | mesures alternatives | 
| :------: | :-----------------------: | :-----------------: | :------------------: |
| Contacter un expert | Numéro de téléphone ou mail | Légitime | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| obtenir un devis / souscription d’offres d’énergie et de services | Données personnelles : Identifiants de l’espace client (login + mot de passe).
| ------------ | ----------------------- | ----------------------- | ----------------------- |
Nom de la société de l’utilisateur, sexe, nom, prénom, email, téléphone. | Obligatoire | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| recevoir la Newsletter | email, type d’utilisateurs (services publics, entreprises, syndics&copropriétés). | Obligatoire | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| Créer un espace client | Données personnelles : sexe, Nom, prénom, email, téléphone fixe, téléphone mobile | Obligatoire | N/A |

## Airbus

| Finalité               | Type de collecte/controle | Nature de la mesure | mesures alternatives | 
| :------: | :-----------------------: | :-----------------: | :------------------: |
| trombinoscope des employés | Les photos sont considérées comme des données personnelles. Vous devez donc obtenir l’accord de toutes les personnes concernées avant d’afcher leurs photos. Si l’une d’entre elles refuse, vous ne pouvez afcher sa photo. | légitime | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| transfert hors réseau corporate de PII | Le transfert de données personnelles concernant un employé ou un tiers sur un support amovible, comme une clé USB, représente un risque particulièrement élevé et ne peut être effectué que dans des circonstances exceptionnelles. Par conséquent, vous devez commencer par demander l’autorisation à votre manager. Si votre manager accepte cette demande, vous devez veiller à toujours utiliser un support chiffré autorisé par Airbus | très encadrée donc légitime | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| santé et bien-être des employés | Il est interdit de traiter des données sensibles – notamment concernant la santé,la génétique, les données biométriques, les convictions politiques, religieuses ou philosophiques, les pratiques et orientations sexuelles, l’adhésion à un syndicat, les origines raciales ou ethniques, le casier judiciaire – à moins que la loi ne l’exige ou que la personne concernée n’ait donné expressément son accord préalable. | très très encadrée et soumise à la loi et/ou accord préalable de la personne concernée donc légitime | mesure complémentaire : anonymisation des données en plus de l’accord ? |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| informations sur la présence des personnes sur le site | Contrôle des accès physiques aux sites par badge (toute personne pénétrant sur les sites Airbus), et pointage électronique par badgeage (employés) | obligatoire pour une entreprise de cette taille et de cette nature | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| prévenir les intrusions dans le système via support USB | monitoring des flux sur les ports USB des  machines de travail et blocage physique des ports USB sur les machines de contrôle industriel (données anonymisées) | obligatoire afin d’éviter des attaques sur les systèmes de contrôle industriels | blocage pur et simple des ports USB sur tout le parc (mesure contraignante) |

## Total direct energie

| Finalité | Type de collecte/controle | Nature de la mesure | mesures alternatives | 
| :------: | :-----------------------: | :-----------------: | :------------------: |
| Exécution du contrat (Contractuel) | Données personnelles (Coordonées - Données d’identification Information liées à votre logement et vos besoins énergétiques Données contractuelles Données de paiement) | Obligatoire | |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| Analyses statistiques et d’amélioration de la qualité des services. | Statistique d’utilisation application - sites (Comportement, Actions, Avis, Mails, Appels, informations des communications.) | Sous réserve de consentement | Formulaire de satisfaction de l’application |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| Message publicitaires, communication promotionnelle | Données personnelles (Données démographiques, Taux de clics publicitaires, Autre données obtenues par le biais de partenaires) | Sous réserve de consentement | |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| Amélioration de la stabilité | Modèle de terminal, réseau, paramètres de l’application, informations relatives à la connexion sur l’application. | Intrusive - Sous réserve de consentement | | 


## Vinci autoroute

| Finalité | Type de collecte/controle | Nature de la mesure | mesures alternatives | 
| :------: | :-----------------------: | :-----------------: | :------------------: |
| l’inscription aux services que l’entreprise propose | Les données nécessaires à l’inscription aux services que nous proposons (par exemple, l’abonnement au service télépéage, les applications mobiles) : vos noms et prénoms, civilité, numéro de téléphone, adresse e-mail, date de naissance, adresse postale, historique des échanges entre vous et VINCI Autoroutes ou ses filiales, mot de passe, plaque d’immatriculation, données bancaires. Certaines de ces informations sont obligatoires. Si vous ne souhaitez pas les communi- quer, nous ne serons pas en mesure de vous fournir l’accès aux services proposés. | nécessaire sous condition de la mise en place de moyens pour sécuriser les dites données | N/A |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| collecte de données de trajets pour calcul facture | Les données relatives à vos déplacements sur autoroute afin de calculer le montant du trajet effectué (par exemple, la date, la gare de péage, l’heure d’entrée et de sortie de l’autoroute). | légitime afin de calculer le montant de la facturation des clients | La durée (heure d’entrée et de sortie) est-elle vraiment nécessaire ? |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| maintenance et qualité des services | Les données que nous sommes susceptibles de vous demander lorsque vous nous contactez ou lorsque vous nous signalez un problème relatif à nos services (par exemple, votre nom et prénom, votre numéro de téléphone)  | intrusif | mise en place d’un système de rapports anonymes |
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| statistiques ? non explicitement précisé | Les données liées à votre localisation lorsque vous avez accepté la collecte et le traitement de ce type de données. | intrusif mais soumis à acceptation du client | expliciter la finalité derrière cette collecte de données + anonymisation des données si leur collecte relève de fins statistiques | 
| ------------ | ----------------------- | ----------------------- | ----------------------- |
| Statistiques, amélioration des services & publicité | Lors de la navigation sur notre site internet ou de l’utilisation d’une application mobile proposée par VINCI Autoroutes ou ses filiales, et après avoir obtenu votre accord, nous sommes susceptibles de collecter, par le biais de « cookies », des informations relatives aux appareils ou aux réseaux à partir desquels vous accédez à nos services. | pas assez précis, potentiellement intrusif | préciser les fins de cette collecte de données et éventuellement les anonymiser |


# C - Les responsabilités et obligations de l’Administrateur.

__Nous en avons vus dans notre cours les responsabilités et obligations de l’administrateur. Je vous demande, juste, en reprenant le cours d’ordonner ces points par ordre d’importance décroissante (du point le plus important au moins important). Argumentez vos choix.__

* __Il est compliqué de définir les priorités de l'administrateur tant ses obligations sont importantes.__

1) __Dénonciation__ - Obligation de dénoncer un fait grave tel que la pédopornographie; l’incitation à la haine raciale; l’apologie de crime contre l’humanité; l’organisation d’acte terroriste; atteinte à l’ordre public ou à la sécurité de l’Etat, atteinte à la vie d’autruis. Tout cela passe avant le reste au niveau de la gravité des faits.

2) __Alerte__ - L’administrateur a l’obligation d’alerter / informer lors d’un comportement suspect / d’une intrusion / d’une fuite impliquant directement la sécurité du réseau ou de données personnelles. 

3) __Loyauté__ - L’administrateur se doit d’être impliqué dans son travail, son entreprise. La loyauté implique une obligation de conseil, d’information, d’alerte et “mitigation” qui obligent à faire le nécessaire pour répondre à la demande du client. Elle sert de base pour la Finalité, la sécurité et la  proportionnalité. Il faut faire preuve d’éthique et ne pas prendre de mesures abusives.

4) __Transparence__ - L’administrateur se doit d’être aussi transparent que possible sur ses actions et celle qu’il a pu observer, il se doit d'avertir les salariés sur le traitement et la finalité de leurs données personnelles.

5) __Confidentialité__ - L’administrateur gère toutes les données à caractère personnel de l’entreprise, souvent des bases de données comprenant des nom, prénom, numéros de sécurité social, donnée bancaire, etc. Il doit veiller sur la confidentialité, la disponibilité et l’intégrité de ces données. 

6) __Fidélité__ -  Les missions de l’administrateur doivent être conformes à la politique de l’entreprise et à sa philosophie, comme au travers d’une charte informatique mais aussi ne pas dévoiler d’information sur son client aux concurrents de son client. Il faut que l’administrateur pense à demander l’aval de son client avant de partager une quelconque information.