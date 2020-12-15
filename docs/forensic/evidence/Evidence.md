Ressource :

 * https://github.com/Invoke-IR/ForensicPosters
 * https://digital-forensics.sans.org/community/posters

# 1 Prérequis :

Déchiffrer l'image avec GPG :
````bash
gpg Evidence.vmdk_bak.gpg
````

Ensuite, je rattache le VMDK déchiffré à la machine sur VMWARE Caine.

Je monte le disdque avec Mounted (petit truc vert en bas à gauche dans Caine).

Je vérifie le hash de l'image :
````bash
sudo md5sum /media/sdb1/Windows/memory.img
04b16c5a3ae70bef40e120fc821bee85

sudo md5sum /media/sdb1/Windows/disk.raw
415689cdfb3928e10a9f3786bb650e05

04b16c5a3ae70bef40e120fc821bee85  memory.img
415689cdfb3928e10a9f3786bb650e05  disk.raw
````

---

# 2 Analyse de la RAM :

Je détermine l'image info de la RAM :
````bash
/home/student/training/tools/volatility -f /media/sdb1/Windows/memory.img  imageinfo
````

Retour de volatility :
````text
Volatility Foundation Volatility Framework 2.5
INFO    : volatility.debug    : Determining profile based on KDBG search...

          Suggested Profile(s) : Win10x86, Win8SP0x86, Win81U1x86, Win8SP1x86, Win10x86_44B89EEA
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/media/sdb1/Windows/memory.img)
                      PAE type : PAE
                           DTB : 0x1a8000L
                          KDBG : 0x82461820L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x8248b000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2016-08-17 12:00:47 UTC+0000
     Image local date and time : 2016-08-17 14:00:47 +0200
`````

Comme on sais que c'est du Windows, on lance la commande pslist :
````bash
time /home/student/training/tools/volatility -f /media/sdb1/Windows/memory.img pslist
`````

Ca n'a pas marché il faut utiliser autre chose :
`````bash
time /home/student/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --profile=Win10x86 pslist # 11 secondes
time /home/student/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --profile=Win8SP0x86 pslist # 19 secondes
time /home/student/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --profile=Win10x86_44B89EEA pslist # 7 secondes
`````

Avec le dernier profile ca a bien marché pas de problème d'encodage des carctères comme avec les deux premiers profils.

Ensuite, on essaye à partir des adresses des pointeurs (DTB,KDBG, KPCR) retourner les processus :

`````bash
time /home/student/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --dtb 0x1a8000 --kdbg 0x82461820 --kpcr 0x8248b000 --profile=Win10x86_44B89EEA pslist # 2 secondes
`````

Si on est sur des machines Windowsdans la réalité, il feut prendre le temps de spécifier les paramètres **DTB**, **KDBG**, **KPCR** ca va aller beacoup plus vite. Dans notre cas en spécifiant les paramètres on à mis **2 secondes** la ou on met **7 secondes** sans ces paramètres.

Ensuite on l'enregistre dans les variables d'environment pour ne pas avoir a tout retaper :
````bash
alias vol="sudo /home/student/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --profile=Win10x86_44B89EEA --dtb=0x1a8000 --kdbg=0x82461820 --kpcr=0x8248b000"
````

Ce qui nous permet de tapper **vol commande** sans avoir à tout retaper.
````bash
vol pslist
````

Retour :
````text
Volatility Foundation Volatility Framework 2.5
Offset(V)  Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
---------- -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0x868a7700 System                    4      0    104        0 ------      0 2016-08-16 12:54:24 UTC+0000                                 
0x8d2af5c0 smss.exe                244      4      2        0 ------      0 2016-08-16 12:54:24 UTC+0000                                 
0x8f7e3040 csrss.exe               324    316     10        0      0      0 2016-08-16 12:54:27 UTC+0000                                 
0x9487c640 smss.exe                388    244      0 --------      1      0 2016-08-16 12:54:28 UTC+0000   2016-08-16 12:54:28 UTC+0000  
0x8b9bf300 wininit.exe             396    316      2        0      0      0 2016-08-16 12:54:28 UTC+0000                                 
0x8f71d2c0 csrss.exe               408    388     11        0      1      0 2016-08-16 12:54:28 UTC+0000                                 
0x94863c40 winlogon.exe            460    388      4        0      1      0 2016-08-16 12:54:28 UTC+0000                                 
0x8b9bc300 services.exe            488    396      6        0      0      0 2016-08-16 12:54:29 UTC+0000                                 
0x948c3040 lsass.exe               516    396      7        0      0      0 2016-08-16 12:54:29 UTC+0000                                 
0x948fb180 svchost.exe             576    488     19        0      0      0 2016-08-16 12:54:30 UTC+0000                                 
0x94954380 svchost.exe             620    488     10        0      0      0 2016-08-16 12:54:30 UTC+0000                                 
0x949bdc40 dwm.exe                 716    460     13        0      1      0 2016-08-16 12:54:31 UTC+0000                                 
0x949b08c0 svchost.exe             764    488     16        0      0      0 2016-08-16 12:54:31 UTC+0000                                 
0x9495d6c0 svchost.exe             800    488     46        0      0      0 2016-08-16 12:54:31 UTC+0000                                 
0x949d3040 svchost.exe             848    488     24        0      0      0 2016-08-16 12:54:31 UTC+0000                                 
0x949d3c40 svchost.exe             856    488     10        0      0      0 2016-08-16 12:54:31 UTC+0000                                 
0x949faac0 svchost.exe             896    488     22        0      0      0 2016-08-16 12:54:31 UTC+0000                                 
0x94ca1700 svchost.exe            1068    488     24        0      0      0 2016-08-16 12:54:32 UTC+0000                                 
0x94caf040 svchost.exe            1132    488     24        0      0      0 2016-08-16 12:54:32 UTC+0000                                 
0x9a018040 spoolsv.exe            1212    488     10        0      0      0 2016-08-16 12:54:32 UTC+0000                                 
0x9a039040 svchost.exe            1380    488     12        0      0      0 2016-08-16 12:54:34 UTC+0000                                 
0x9a118380 svchost.exe            1540    488      7        0      0      0 2016-08-16 12:54:34 UTC+0000                                 
0x9a10cb00 wlms.exe               1572    488      4        0      0      0 2016-08-16 12:54:34 UTC+0000                                 
0x9c64f980 sihost.exe              688    800     12        0      1      0 2016-08-16 12:55:35 UTC+0000                                 
0x8c13ea00 taskhostw.exe           268    800      9        0      1      0 2016-08-16 12:55:36 UTC+0000                                 
0x8ad6c040 userinit.exe           1556    460      0 --------      1      0 2016-08-16 12:55:36 UTC+0000   2016-08-16 12:55:59 UTC+0000  
0x8ac4a040 explorer.exe           2068   1556     57        0      1      0 2016-08-16 12:55:36 UTC+0000                                 
0x8ad60940 RuntimeBroker.         2196    576     21        0      1      0 2016-08-16 12:55:37 UTC+0000                                 
0x8ad5f040 SkypeHost.exe          2220    576     10        0      1      0 2016-08-16 12:55:37 UTC+0000                                 
0x8ad22c40 ShellExperienc         2432    576     38        0      1      0 2016-08-16 12:55:39 UTC+0000                                 
0x8b8520c0 SearchIndexer.         2532    488     17        0      0      0 2016-08-16 12:55:40 UTC+0000                                 
0x8b8fb8c0 OneDrive.exe           3592   2068     14        0      1      0 2016-08-16 12:55:57 UTC+0000                                 
0x9c68ec40 fontdrvhost.ex         4428    460      6        0      1      0 2016-08-16 12:57:09 UTC+0000                                 
0x9c728480 svchost.exe            4900    488      3        0      1      0 2016-08-16 12:57:21 UTC+0000                                 
0x8ad86c40 Skype.exe              5128   4696     64        0      1      0 2016-08-16 12:57:42 UTC+0000                                 
0x8c0c9240 TrustedInstall         6108    488      4        0      0      0 2016-08-16 12:58:24 UTC+0000                                 
0x8c0ba9c0 TiWorker.exe           6140    576      5        0      0      0 2016-08-16 12:58:25 UTC+0000                                 
0x9d489780 SystemSettings         2144    576      4        0      1      0 2016-08-16 12:59:36 UTC+0000                                 
0x9499ac40 ApplicationFra         1696    576      5        0      1      0 2016-08-16 12:59:48 UTC+0000                                 
0x9c629300 SystemSettings         5268   5252      4        0      1      0 2016-08-16 12:59:51 UTC+0000                                 
0xb0d47780 svchost.exe            4888   4748      2        0      1      0 2016-08-16 13:02:57 UTC+0000                                 
0x9d5e74c0 explorer.exe           4872   4748      3        0      1      0 2016-08-16 13:02:58 UTC+0000                                 
0x9c7d7c40 svchost.exe            2168   5860      2        0      1      0 2016-08-16 13:03:04 UTC+0000                                 
0xb0c96740 update.exe             5172   5860      6        0      1      0 2016-08-16 13:03:04 UTC+0000                                 
0xd0d9f600 cmd.exe                1976   5172      0 --------      1      0 2016-08-16 13:04:47 UTC+0000   2016-08-16 13:07:36 UTC+0000  
0x9d5ba900 cmd.exe                 736   5172      0 --------      1      0 2016-08-16 13:07:40 UTC+0000   2016-08-16 13:43:12 UTC+0000  
0xbac89640 SystemSettings         4968    576     26        0      1      0 2016-08-16 13:41:14 UTC+0000                                 
0xbad4b040 cmd.exe                2748   5172      0 --------      1      0 2016-08-16 13:50:51 UTC+0000   2016-08-16 14:08:30 UTC+0000  
0xbf755c40 cmd.exe                5280   5172      0 --------      1      0 2016-08-16 14:17:24 UTC+0000   2016-08-16 14:18:48 UTC+0000  
0x8b8c44c0 cmd.exe                 868   5172      0 --------      1      0 2016-08-16 14:19:45 UTC+0000   2016-08-16 14:23:02 UTC+0000  
0xd53d2c40 cmd.exe                3540   5172      0 --------      1      0 2016-08-16 14:23:05 UTC+0000   2016-08-16 14:23:46 UTC+0000  
0xd5321480 SearchUI.exe           7360    576     26        0      1      0 2016-08-16 18:13:21 UTC+0000                                 
0x9c6a8040 audiodg.exe           18084    848      7        0      0      0 2016-08-17 12:00:20 UTC+0000                                 
0xc8606c40 RamCapture.exe        16740   2068      4        0      1      0 2016-08-17 12:00:36 UTC+0000                                 
0xd53a3500 conhost.exe           16756  16740      2        0      1      0 2016-08-17 12:00:36 UTC+0000                                 
0x9c61a300 SearchProtocol        15756   2532      7        0 ------      0 2016-08-17 12:00:50 UTC+0000                                 
0xc7fa2a40 SearchFilterHo        14288   2532      5        0 ------      0 2016-08-17 12:00:50 UTC+0000                                 
0xe2df3040 MusNotificatio        16968    800      1        0 ------      0 2016-08-18 09:25:38 UTC+0000                                 
0xb0df7040 ?q???q??                  0      0 22...6 -------- ------      0  
````

Utilisation des YARA rules :
````bash
cd /home/student/training/ex1/yara-rules
vol yarascan -y index.yar > /home/student/yara.text
````

J'allège un peux l'index .yar pour avoir uniquement les CVE, les malware et les Exploits-Kits :
````bash
cd /home/student/training/ex1/yara-rules
find CVE_Rules/ Exploit-Kits/ malware/ -name "*.yar" -exec echo include \"`pwd`/{}\" \; > test.yar
````

Je relance ma commande avec mon yara allégé :
````bash
vol yarascan -y test.yar > /home/student/yara-out.txt
````

Obtenir un résumé des règles détecter par YARA rules :
````bash
grep 'Rule:' yara-out.txt  | sort | uniq -c
````

Retour :
````text
15 Rule: SharedStrings
3 Rule: spyeye_plugins
9 Rule: UPX
51 Rule: with_sqlite
18 Rule: Xtreme
9 Rule: xtreme_rat
19 Rule: xtremrat
````

Bon on a des RAT ca c'est inquiétant, ce qui peut être intéréssant de voir cart on a 15 share string c'est de voir le contenu de ce qui à topper cette catégorie.

Retour des sharedStrings  :
````bash
cd /home/student/
grep -Rl 'rule SharedStrings' *
cd /home/student/training/ex1/yara-rules
````

Retour :
````text
training/ex1/yara-rules/malware/MALW_LURK0.yar
````

Cette YARA rule liste plsuieurs IOC, dans notrze cas on à juste les données **E..R**, qui ont permis de matcher pour les SharedStrintgs.

A chaque fois que l'on match sur une YARA rule il faut regarder plus en profondeur pour déterminer si c'est un faux positif.
Dans notre casx la c'etait un faux positif.

Résumé :
 * On a déterminer l'image de Windows précisement par le temps qul profil était le plus rapide est lequel n'afficher pas des **?**,
 * On à determiner le **DTB**, **KDBG**, **KPCR** diminuer le temps de traitement des recherche dans la RAM,
 * On a vu avec les grep les règles qui ont été détecté par les YARA rules (RAT -> critique),
 * On a regarder la YARA rule en relation avec Shared Strings,
 * On a déterminé que c'est un faux positif pour les shared strings,

Exercice analyse avec les autres autres alertes.

---

Avec l'alerte xtreme_rat :
````bash
grep -Rl 'rule xtreme_rat' *
cd /home/student/training/ex1/yara-rules
````

Retour :
````text
training/ex1/yara-rules/malware/RAT_Xtreme.yar
````

Identification de la rèle dans le fichier :
````bash
cat training/ex1/yara-rules/malware/RAT_Xtreme.yar
````

Voci la YARA rule de détection pour xtreme_rat :
````text
rule xtreme_rat : Trojan
{
	meta:
		author="Kevin Falcoz"
		date="23/02/2013"
		description="Xtreme RAT"
	
	strings:
		$signature1={58 00 54 00 52 00 45 00 4D 00 45} /*X.T.R.E.M.E*/
		
	condition:
		$signature1
}
````

Identification des processus :
     
* Process svchost.exe Pid 4888
* Process explorer.exe Pid 4872
* Process update.exe Pid 5172

---

Avec l'alerte UPX :
````bash
grep -Rl 'rule UPX' *
cd /home/student/training/ex1/yara-rules
````

Retour :
````text
training/ex1/yara-rules/malware/RAT_Ratdecoders.yar
````

Identification des process :
````bash
 grep -i -A 1 'UPX' /home/student/yara-out.txt  | grep Owner | uniq -c
````

Retour :
````text
3 Owner: Process svchost.exe Pid 4888
3 Owner: Process explorer.exe Pid 4872
3 Owner: Process update.exe Pid 5172
````

Avec l'alerte xtremrat :
````bash
grep -Rl 'rule xtremrat' *
cd /home/student/training/ex1/yara-rules
````

Retour :
````text
training/ex1/yara-rules/malware/RAT_Xtreme.yar
````

Identification des process :
````bash
 grep -i -A 1 'xtremrat' /home/student/yara-out.txt  | grep Owner | uniq -c
````

Retour :
````text
11 Owner: Process explorer.exe Pid 4872
8 Owner: Process update.exe Pid 5172
````


On a trouvé beaucoup d'occupances pour
     * SQLite - non exploré à ce jour
     * Shared Strings, probablement faux positif (STRINg E.R trop génrique)
     * SpyEye, probablement un faux positif vu les chaines recherchées
     * Un packet détecté (UPX)
     * probable rat xtrem_rat

- On se concentre sur les processus infectés par le packer et le xtrem_rat
  PID 4888 (svchost)
  PID 4872 explorer
  PID 5172 update

SQLITE difficiele de dire si c'est des vrais postifis ou pas.
Refaire la timeline de l'atatque.

Résumé : :
J'ai vérifié le MD5 du dump disk et lmémoire (ok)

* Mettre les valeurs des hash

On a trouvé l'empreinte de l'os avec le plugin imageinfo Win10_ ????
On a trouvé DTB KPCR et cpi

* citer les adresses mémoire

Nous avons appliqué les yara rules sur le dump mémoire, en nous concentrant sur: CVE, malware, packers
On a trouvé beaucoup d'occupances pour

* SQLite - non exploré à ce jour
* Shared Strings, probablement faux positif (STRINg E.R trop génrique)
* SpyEye, probablement un faux positif vu les chaines recherchées
* Un packet détecté (UPX)
* probable rat xtrem_rat

On se concentre sur les processus infectés par le packer et le xtrem_rat

* PID 4888 (svchost)
* PID 4872 explorer
* PID 5172 update

## 2.1 Retracer la timeline de l'attaque :

Observer le sprocessus :
````bash
vol pslist
````

Un ligne est intéréssante :
````text
0x868a7700 System                    4      0    104        0 ------      0 2016-08-16 12:54:24 UTC+0000
`````

Le processus **System** est le premier processus qui démarre lors du démarrage du système.
Donc le système à boot le 16 Aout 2016 à 12:54:24.

Ensuite, les serices applicatifs démarre chacun leurs tour.

Voci les processus que l'on suspecte :

* svchost.exe,
* explorer.exe,
* update.exe,
* 6 processus cmd.exe,


On peux remarquer que le PPID des processus **cmd.exe** est identique entre tous les process, le PPID **5172** qui correspond au processus **update.exe**.

Donc :

* BOOT PC, System 	:  2016-08-16 12:54:24 UTC+0000
* UPDATE.EXE 		:  2016-08-16 13:03:04 UTC+0000

Nosu pouvons observer que le processus UOPDATE.EXE lance un processus CMD.EXE toutes les 3 minutes, c'est louche...

Ce qui est intéréssant d'observer c'est comment les processus ont été lancé :

* Pour svchost.exe
````bash
vol dlllist -p 4888 | grep 'Command line'
````

Retour :
````text
Command line : svchost.exe
````

Il à été lancé par la CLI.

* Pour update.exe :
````bash
vol dlllist -p 5172 | grep 'Command line'
````

Retour :
````text
Command line : C:\Users\Peter\AppData\Roaming\HostData\update.exe 
````

Il à été lancé par la CLI.
Bizzard update.exe se trouve dans uh répertoire ou il ne doit pas être normalement...

* Pour explorer.exe :
````bash
vol dlllist -p 4872| grep 'Command line'
````

Retour :
````text
Command line : explorer.exe
````

Il à été lancé par la CLI.

---

## 2.2 Analyse des processus : 

---

### 2.2.1 EXPLORER.EXE :
Pour explorer.exe :
````bash
vol pslist | egrep '(Name|explorer.exe)'
````

Retour :
````text
explorer.exe           2068   
explorer.exe           4872
````

Bizzard deux processus explorer.exe alors que normalement il n'y en a q'un !


Le PPID de 2068 est 1156 :
````bash
vol pslist | grep 1556 
````

Retour :
````text
userinit.exe           1556
````

C'est un peu plus cohérant...

On a possiblement identifié :
* Un processus explorer.exe, sain PID:2068
* Un processus explorer.exe, vérolé PID:4872

Très probablement il y a un mecanisme qui permet de créer deux process explorer.exe.

---

### 2.2.1 UPDATE.EXE :
On a qu'un procesuss UDATE.EXE -> OK

## 2.3 Analyse réseau :
````bash
vol netscan
````

Lorsque le PID == -1 c'est que volatility n'arrive pas a retrouver el PID du processus...
On peux noter l'utilisation de ports de destination étrange **12345** alors que la connexion est en état **ESTABLISHED** et a chaque fois on a pas l'@ IP de destination...


Recherche spécifique sur le port de destination **12345**, a noter le port de destination **33033** est étrange... :
````bash
vol netscan | egrep '(State|:12345|:33033)' 
````

Retour :
````text
192.168.5.100:59220            -:12345              ESTABLISHED      -1 
192.168.5.100:59271            -:12345              ESTABLISHED      -1
192.168.5.100:59268            -:33033              CLOSED           -1 
````

Ok, on a vu des ports de destination **80** et **443**... analyse de ces connexions :
````bash
vol netscan | egrep '(State|:80|:443)' 
````

Retour :
````text
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      
0x85b63230         TCPv4    192.168.5.100:59280            -:443                ESTABLISHED      -1
0x86963230         TCPv4    192.168.5.100:59280            -:443                ESTABLISHED      -1
0x8ad0bc30         TCPv4    192.168.5.100:59277            0.0.0.29:80          ESTABLISHED      -1
0x9a1e2c00         TCPv4    192.168.5.100:49864            -:443                ESTABLISHED      -1
0x9d5677b0         TCPv4    192.168.5.100:58959            0.0.0.0:443          ESTABLISHED      -1
0xc6a21308         TCPv4    192.168.5.100:59250            -:443                ESTABLISHED      -1
0xc7278c70         TCPv4    192.168.5.100:59265            -:443                ESTABLISHED      -1
0xc7e81618         TCPv4    192.168.5.100:59246            -:443                ESTABLISHED      -1
0xc7eeadf0         TCPv4    192.168.5.100:59234            -:443                ESTABLISHED      -1
0xc7f9e760         TCPv4    192.168.5.100:59283            -:443                ESTABLISHED      -1
0xd0d33008         TCPv4    192.168.5.100:59269            -:443                ESTABLISHED      -1
0xe2d145c8         TCPv4    192.168.5.100:59274            -:443                CLOSED           -1
````

Humm, à chaque fois on a aucune IP de destination...

Constat, à chaque observation que l'on réalise on n'arrive pas à obtenir l'@IP de destination, ce qui est étrange surtout pour des connexions **ESTABLISHED**. 
Généralement dans un CSIRT toutes les connexions sont tracés avec différentes statistiques (durées, taille des échanges, etc.). Généralement les technologies derrières sont :
 * SPLUNK

Les données des SWITCHS transitent avec NETFLOW, quipermet de logguer les connexions (ICMP,IP,TCP,UDP,etc.).
dans notre cas, la seule chance possible de retrouver l'@ IP de destination c'est avec SPLUNK et NETFLOW.

Pour résumer, je sais qu'un RAT à été déployé et que quelquechose de louche est présente dans le répertoire Appdata grâce aux horodatage des processus..

Recherche avec malfind :
````bash
vol malfind | grep Process
````

Retour :
````text
Process: explorer.exe Pid: 2068 Address: 0x6660000
Process: explorer.exe Pid: 2068 Address: 0x72d0000
Process: Skype.exe Pid: 5128 Address: 0x1f0000
Process: explorer.exe Pid: 4872 Address: 0xc80000
Process: update.exe Pid: 5172 Address: 0x400000
Process: SearchUI.exe Pid: 7360 Address: 0xa7d0000
Process: SearchUI.exe Pid: 7360 Address: 0xc730000
````

Hum ca confirme nos hypothèses...

Recherche des mutants, les mutants sont des handle qui change de structure et cela peut être un IoC :
````bash
vol mutantscan
````

On retrouve skype, ce virus ne semble pas de passer par des mutex

Pour conclure, on a une idée assez précise ou chercher, par le dump du disque, nous pourrons analyser plus en profondeur.

---

# 3 Analyse du disque :

---

## 3.1 Prérequis :
Analyse des partition dump du DD :
````bash
mmls disk.raw
````

Retour :
````text
      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0001026047   0001024000   NTFS / exFAT (0x07)
003:  000:001   0001026048   0050329599   0049303552   NTFS / exFAT (0x07)
004:  -------   0050329600   0050331647   0000002048   Unallocated
````

Deux partition NTFS, généralement la partition C: est la plus grande, je suppose donc que la partion C: est la n°3.

Pour monter la partiton, il faut préciser à partir de quel octet l'on souhaite commencer.
La valeur Start dans le retour de mmls, correspond au numéros de bloc, par défaut dans Windows, les blocs sont de 512 Octets.

Donc :
0001026048 * 512 = 525336576


Puis, monter la partition en **RO**
````bash
mkdir /mnt/partitionC
mount -t ntfs -o ro,offset=525336576 disk.raw /mnt/partitionC/
````

Vérification :
````bash
ls /mnt/partitionC/
````

Retour :
`````text
autoexec.bat  BOOTNXT     pagefile.sys  ProgramData    Recovery      swapfile.sys               Users
bootmgr       config.sys  PerfLogs      Program Files  $Recycle.Bin  System Volume Information  Windows
`````

C'est la partition C: !

---

## 3.2 Analyse avec autopsy :

Créer la timeline


---

## Analise avec clamav

```
clamscan -i -r /mnt/partitionC/ > scanAV.txt
```

```

```

## Firefox crach report
* Il peut-être utile de regarder les crash reports, lors d'une tentative d'exploitation il est possible de générer des crashs.


