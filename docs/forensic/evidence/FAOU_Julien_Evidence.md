---
title: "FAOU_Julien_Evidence"
author: ["Enseignant responsable: Damien Naviliat"]
date: "2020-12-03"
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
code-block-font-size: \scriptsize
---

# Partie 1 

__Schéma de l'attaque telle que vous avez réussi à la reconstruire__

> Les éléments de preuves qui m'ont permis de retrouver le schéma de l'atttaque sont détaillés dans les parties 2 et 3.

1) L'utilisateur se rend sur le blog de son entreprise

2) Le site été compris, injection de code JS, redirection vers le blog d'un autre site.

3) Le cache de son navigateur firefox à été infecté par un RAT (Remote Access Trojan)

4) Le RAT a téléchargé de nombreux outils d'audit depuis un serveur

5) Probablement auditer l'ensemble du parc réseaux et exfiltrer des données.


# Partie 2

__Elements de d'indices collectés dans volatility__

## Informations

> __Le disque Evidence a été monté en READ-ONLY : /media/sdb1/Window/__

> __L'outil volatility se trouve au chemin suivant : ~/training/tools/volatility/vol.py__

## Analyse mémoire

### Systeme informations

```text
sudo ./vol.py -f /media/sdb1/Windows/memory.img imageinfo

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
```

On obtient des versions potentiels ainsi que les adresses de DTB, KDBG et KPCR qu'il faudra préciser.

Après plusieurs essais, le bon profile est : __Win10x86_44B89EEA__

```text
sudo ./vol.py -f /media/sdb1/Windows/memory.img --dtb=0x1a8000 --kdbg=0x82461820 --kpcr=0x8248b000 --profile=Win10x86_44B89EEA pslist

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
```

Pour simplifier les futurs commandes, nous utiliserons un alias.

```text
alias vol="sudo ~/training/tools/volatility/vol.py -f /media/sdb1/Windows/memory.img --dtb=0x1a8000 --kdbg=0x82461820 --kpcr=0x8248b000 --profile=Win10x86_44B89EEA"
```

### Scan Malware

Commençons par scanner pour de potentiels malware, nous allons utiliser les Yara-rules.

Les yara-rules se trouvent dans le dossier : __~/training/ex1/yara-rules/__

Pour éviter des faux-positifs, on va trier ces yara-rules pour ne sélectionner que celles qui sont pertinantes dans notre cas.

```bash
find CVE_Rules/ Exploit-Kits/ malware/ -name "*.yar" -exec echo include \"`pwd`/{}\" \; > test.yar
```

Lançons le scan

````bash
vol yarascan -y test.yar > results.txt
````

Obtenir un résumé des règles détecter par YARA rules :
````bash
grep 'Rule:' results.txt  | sort | uniq -c

15 Rule: SharedStrings
3 Rule: spyeye_plugins
9 Rule: UPX
51 Rule: with_sqlite
18 Rule: Xtreme
9 Rule: xtreme_rat
19 Rule: xtremrat
````

Analysons tout cela plus en détails : 

__SharedStrings__

````bash
grep -Rl 'rule SharedStrings' *

malware/MALW_LURK0.yar
````

```txt
rule SharedStrings : Family {
	meta:
		description = "Internal names found in LURK0/CCTV0 samples"
		author = "Katie Kleemola"
		last_updated = "07-22-2014"
	
	strings:
		// internal names
		$i1 = "Butterfly.dll"
		$i2 = /\\BT[0-9.]+\\ButterFlyDLL\\/
		$i3 = "ETClientDLL"

		// dbx
		$d1 = "\\DbxUpdateET\\" wide
		$d2 = "\\DbxUpdateBT\\" wide
		$d3 = "\\DbxUpdate\\" wide
		
		// other folders
		$mc1 = "\\Micet\\"

		// embedded file names
		$n1 = "IconCacheEt.dat" wide
		$n2 = "IconConfigEt.dat" wide

		$m1 = "\x00\x00ERXXXXXXX\x00\x00" wide
		$m2 = "\x00\x00111\x00\x00" wide
		$m3 = "\x00\x00ETUN\x00\x00" wide
		$m4 = "\x00\x00ER\x00\x00" wide

	condition:
		any of them //todo: finetune this

}
```

```bash 
$m4 = "\x00\x00ER\x00\x00"
``` 

C'est cette ligne qui a fait topé, elle est très générique et ne nous donne vraiment d'information suplémentaire. Probablement un faux positif.


---

__spyeye_plugins__ : Faux positif au vu des chaines recherchées

---

__UPX__

```bash
grep -Rl 'rule UPX' *

training/ex1/yara-rules/malware/RAT_Ratdecoders.yar
```

Identification des processus : 

```bash
grep -i -A 1 'UPX' /home/student/yara-out.txt  | grep Owner | uniq -c

3 Owner: Process svchost.exe Pid 4888
3 Owner: Process explorer.exe Pid 4872
3 Owner: Process update.exe Pid 5172
```

---

__with_sqlite__ : Beaucoup d'occurence, il est difficile de dire si c'est un faux positif ou non, il faudra le déterminer avec la timeline.

---

__xtremrat__

```bash
grep -Rl 'rule xtremrat' *

malware/RAT_Xtreme.yar
```

```text
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
```

Identification des process

```text
grep -i -A 1 'xtremrat' /home/student/yara-out.txt  | grep Owner | uniq -c

11 Owner: Process explorer.exe Pid 4872
8 Owner: Process update.exe Pid 5172
```

On retrouve __ER__ dans la signature : 

```bash
__/*X.T.R.E.M.E*/__  =>  __$m4 = "\x00\x00ER\x00\x00" wide__
```

Identification des processus :

* Process svchost.exe Pid 4888
* Process explorer.exe Pid 4872
* Process update.exe Pid 5172

__xtremrat__ est notre piste la plus plausible.

### Scan des processus

```text
vol pslist

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
```

On peut noter que le système à démarer à __2016-08-16 12:54:24 UTC+0000__

```text
0x868a7700 System                    4      0    104        0 ------      0 2016-08-16 12:54:24 UTC+0000
```

Cherchons les processus infectés vu précedemment

```text
0xb0d47780 svchost.exe            4888   4748      2        0      1      0 2016-08-16 13:02:57 UTC+0000
0x9d5e74c0 explorer.exe           4872   4748      3        0      1      0 2016-08-16 13:02:58 UTC+0000
0xb0c96740 update.exe             5172   5860      6        0      1      0 2016-08-16 13:03:04 UTC+0000                                 
0xd0d9f600 cmd.exe                1976   5172      0 --------      1      0 2016-08-16 13:04:47 UTC+0000   2016-08-16 13:07:36 UTC+0000  
0x9d5ba900 cmd.exe                 736   5172      0 --------      1      0 2016-08-16 13:07:40 UTC+0000   2016-08-16 13:43:12 UTC+0000  
0xbad4b040 cmd.exe                2748   5172      0 --------      1      0 2016-08-16 13:50:51 UTC+0000   2016-08-16 14:08:30 UTC+0000  
0xbf755c40 cmd.exe                5280   5172      0 --------      1      0 2016-08-16 14:17:24 UTC+0000   2016-08-16 14:18:48 UTC+0000  
0x8b8c44c0 cmd.exe                 868   5172      0 --------      1      0 2016-08-16 14:19:45 UTC+0000   2016-08-16 14:23:02 UTC+0000  
0xd53d2c40 cmd.exe                3540   5172      0 --------      1      0 2016-08-16 14:23:05 UTC+0000   2016-08-16 14:23:46 UTC+0000
```

Quelques minutes après le Boot, xtremrat a lancé __svchost.exe__ et __explorer.exe__. Puis __update.exe__ à lancé plusieurs __cmd.exe_ à quelques minutes d'intervales. C'est suspect.

Il est possible de voir comment le processus a été lancé

__4888__

```bash
vol dlllist -p 4888 | grep "Command line"

Command line : svchost.exe
```

__4872__

```bash
vol dlllist -p 4872 | grep "Command line"

Command line : explorer.exe
```

__5172__

```bash
vol dlllist -p 5172 | grep "Command line"

Command line : C:\Users\Peter\AppData\Roaming\HostData\update.exe
```

__1976__

```bash
vol dlllist -p 1976 | grep "Command line"
```

On peut voir que update.exe a été lancé depuis un repertoire utilisateur : __C:\Users\Peter\AppData\Roaming\HostData\update.exe__

De plus, il y a 2 processus __explorer.exe__, il devrait en avoir qu'un seul !

Si on regarde comment à été lancé le premier explorer.exe

```bash
vol dlllist -p 2068 | grep "Command line"

Command line : C:\Windows\Explorer.EXE
```

Celui-ci est véridicte.

## Analyse des traces réseaux

```bash
vol netscan

Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x85b63230         TCPv4    192.168.5.100:59280            -:443                ESTABLISHED      -1                      
0x86963230         TCPv4    192.168.5.100:59280            -:443                ESTABLISHED      -1                      
0x8ada4678         UDPv4    127.0.0.1:512                  *:*                                   5128     Skype.exe      2016-08-16 12:57:46 UTC+0000
0x8ad0bc30         TCPv4    192.168.5.100:59277            0.0.0.29:80          ESTABLISHED      -1                      
0x8c15e930         UDPv4    0.0.0.0:0                      *:*                                   1132     svchost.exe    2016-08-17 12:01:09 UTC+0000
0x8c15e930         UDPv6    :::0                           *:*                                   1132     svchost.exe    2016-08-17 12:01:09 UTC+0000
0x8c16c008         UDPv4    0.0.0.0:512                    *:*                                   5128     Skype.exe      2016-08-17 12:01:04 UTC+0000
0x9490d480         UDPv4    0.0.0.0:512                    *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x9492fbd8         UDPv4    0.0.0.0:0                      *:*                                   800      svchost.exe    2016-08-16 12:57:14 UTC+0000
0x94975f40         UDPv4    192.168.5.100:512              *:*                                   4        System         2016-08-17 12:00:28 UTC+0000
0x9497e008         UDPv6    fe80::28b6:9b1e:817d:11e5:5888 *:*                                   848      svchost.exe    2016-08-17 12:00:24 UTC+0000
0x94980a08         UDPv4    0.0.0.0:0                      *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x94980a08         UDPv6    :::0                           *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x949e14a8         UDPv4    0.0.0.0:0                      *:*                                   5128     Skype.exe      2016-08-16 12:57:46 UTC+0000
0x9a07c008         UDPv4    0.0.0.0:0                      *:*                                   5128     Skype.exe      2016-08-16 12:57:50 UTC+0000
0x9a07c008         UDPv6    :::0                           *:*                                   5128     Skype.exe      2016-08-16 12:57:50 UTC+0000
0x9a1986d0         UDPv4    0.0.0.0:512                    *:*                                   5128     Skype.exe      2016-08-16 12:57:50 UTC+0000
0x9a1aac18         UDPv4    0.0.0.0:5888                   *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x9a1aac18         UDPv6    :::5888                        *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x9a1e2c00         TCPv4    192.168.5.100:49864            -:443                ESTABLISHED      -1                      
0x9a1f3248         TCPv4    192.168.5.100:49847            -:12350              ESTABLISHED      -1                      
0x9c604050         UDPv4    192.168.5.100:512              *:*                                   4        System         2016-08-17 12:00:28 UTC+0000
0x9c61f418         UDPv4    0.0.0.0:5888                   *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x9c61f418         UDPv6    :::5888                        *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0x9c653208         UDPv4    0.0.0.0:0                      *:*                                   5128     Skype.exe      2016-08-16 12:57:47 UTC+0000
0x9c653208         UDPv6    :::0                           *:*                                   5128     Skype.exe      2016-08-16 12:57:47 UTC+0000
0x9c739e40         UDPv4    0.0.0.0:0                      *:*                                   5128     Skype.exe      2016-08-16 12:57:47 UTC+0000
0x9c7f9228         UDPv4    0.0.0.0:512                    *:*                                   5128     Skype.exe      2016-08-16 12:57:50 UTC+0000
0x9d5677b0         TCPv4    192.168.5.100:58959            0.0.0.0:443          ESTABLISHED      -1                      
0xb0c1d3e0         UDPv4    0.0.0.0:0                      *:*                                   1132     svchost.exe    2016-08-17 12:00:57 UTC+0000
0xb0c1d3e0         UDPv6    :::0                           *:*                                   1132     svchost.exe    2016-08-17 12:00:57 UTC+0000
0xb9cf7a88         UDPv4    127.0.0.1:512                  *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xbad72db0         UDPv6    fe80::28b6:9b1e:817d:11e5:5888 *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xbece84f8         UDPv4    192.168.5.100:512              *:*                                   5128     Skype.exe      2016-08-17 12:01:04 UTC+0000
0xbed24df0         TCPv4    192.168.5.100:59220            -:12345              ESTABLISHED      -1                      
0xbf65e218         TCPv4    192.168.5.100:59271            -:12345              ESTABLISHED      -1                      
0xc5cd2150         UDPv4    192.168.5.100:512              *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xc6a698c8         UDPv6    ::1:5888                       *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xc6a21308         TCPv4    192.168.5.100:59250            -:443                ESTABLISHED      -1                      
0xc7278c70         TCPv4    192.168.5.100:59265            -:443                ESTABLISHED      -1                      
0xc7eacdb0         UDPv4    127.0.0.1:512                  *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xc7eace78         UDPv6    ::1:5888                       *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xc7ff31c0         UDPv4    192.168.5.100:512              *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xc7e81618         TCPv4    192.168.5.100:59246            -:443                ESTABLISHED      -1                      
0xc7eeadf0         TCPv4    192.168.5.100:59234            -:443                ESTABLISHED      -1                      
0xc7f9e760         TCPv4    192.168.5.100:59283            -:443                ESTABLISHED      -1                      
0xc865b008         UDPv6    fe80::3817:3c8c:3f57:fa9b:5888 *:*                                   848      svchost.exe    2016-08-17 12:00:25 UTC+0000
0xd0ccdd08         UDPv4    0.0.0.0:5888                   *:*                                   896      svchost.exe    2016-08-18 09:25:39 UTC+0000
0xd0ccdd08         UDPv6    :::5888                        *:*                                   896      svchost.exe    2016-08-18 09:25:39 UTC+0000
0xd0d33008         TCPv4    192.168.5.100:59269            -:443                ESTABLISHED      -1                      
0xd0dc2278         TCPv4    192.168.5.100:59268            -:33033              CLOSED           -1                      
0xd5216c68         UDPv4    0.0.0.0:512                    *:*                                   1132     svchost.exe    2016-08-17 12:00:28 UTC+0000
0xe2d145c8         TCPv4    192.168.5.100:59274            -:443                CLOSED           -1                      
0xf5d07008         UDPv6    fe80::28b6:9b1e:817d:11e5:5888 *:*                                   856      svchost.exe    2016-08-17 12:00:25 UTC+0000
```

On peut voir différentes connections vers des ports TCP peu communs, vers des destinations inconnues, pourant établies...  :

```text
0x9a1f3248         TCPv4    192.168.5.100:49847            -:12350              ESTABLISHED      -1                      
0xbed24df0         TCPv4    192.168.5.100:59220            -:12345              ESTABLISHED      -1                      
0xbf65e218         TCPv4    192.168.5.100:59271            -:12345              ESTABLISHED      -1                      
0xd0dc2278         TCPv4    192.168.5.100:59268            -:33033              CLOSED           -1
```

### Recapitulatif de l'analyse mémoire

* Le systeme est infecté par un RAT nommé xtreme
* Le malware se cache derriere des noms de processus officiels (explorer.exe)
* Des connections TCP étranges relevées
* Le deuxieme processus explorer.exe a été lancé depuis un répertoire utilisateur et a lancé de mutliples __cmd.exe__.

# Partie 3

__Elements de preuve collectés via caine (sans volatility)__

## Analyse du disque

Il nous faut dans un premier temps repérer les partitions

```bash
sudo mmls /media/sdb1/Windows/disk.raw 

Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0001026047   0001024000   NTFS / exFAT (0x07)
003:  000:001   0001026048   0050329599   0049303552   NTFS / exFAT (0x07)
004:  -------   0050329600   0050331647   0000002048   Unallocated
```

Cette partition est la principale, c'est la plus grosse.

```text
003:  000:001   0001026048   0050329599   0049303552   NTFS / exFAT (0x07)
```

Il est précisé __Units are in 512-byte sectors__, pour monter la partition il faut préciser l'offset : 

```text
1026048 * 512 = 525336576
```

```bash
sudo mkdir /mnt/partition
sudo mount -t ntfs -o ro,offset=525336576 /media/sdb1/Windows/disk.raw /mnt/partition/
ls /mnt/partition/

autoexec.bat  BOOTNXT     pagefile.sys  ProgramData    Recovery      swapfile.sys               Users
bootmgr       config.sys  PerfLogs      Program Files  $Recycle.Bin  System Volume Information  Windows
```

Lançons __autopsy__ et créons un nouveau cas avec le disque dur : 

* Créer un nouveau cas.
* Ajouter l'image disque __/media/sdb1/windows/disk.raw__.
* Selectionner la plus grande partition.
* Lancer un __File Activity Time Line__ sur la partition.

    1) __Create Data File__ et selectionner la partition.
    
    ```text
    Running fls -r -m on vol2
    Body file saved to /usr/share/caine/report/autopsy/EvidenceC/WindowsEvidence/output/body
    Entry added to host config file
    Calculating MD5 Value
    MD5 Value: 139C867C50F5C5FC39C69FAB00A50043
    ```

    2) __Create Timeline__
        * Bien préciser la date de début en se basant sur la date de lancement de l'ordi __2016-08-16 12:54:24 UTC+0000__.
        * On obtient le timeline complet.

```bash
cat /usr/share/caine/report/autopsy/EvidenceC/WindowsEvidence/output/timeline.txt | grep update.exe

86 macb r/r--x--x--x 0        0        101287-48-2 D:/Users/Peter/AppData/Roaming/HostData/update.exe ($FILE_NAME)
61440 ..c. r/r--x--x--x 0        0        101287-128-1 D:/Users/Peter/AppData/Roaming/HostData/update.exe
```

> M : fichier modidifié
> A : Accès au fichier
> C : Metadata changées
> B : fichier créé

On voit que le fichier __D:/Users/Peter/AppData/Roaming/HostData/update.exe__ a bien été ajouté.

## Scan antivirus

Scannons la partition précédement montée à l'aide de l'antivirus __clamav__

```text
sudo clamscan -i -r /mnt/partition/ > ~/clamscan.txt
cat ~/clamscan.txt

/mnt/partition/Users/Peter/AppData/Local/Microsoft/Windows/INetCache/IE/R81B6P1C/3568226350[1].exe: Win.Trojan.Xtreme-7 FOUND
/mnt/partition/Users/Peter/AppData/Local/Mozilla/Firefox/Profiles/z0l7z3kd.default/cache2/entries/394A23D50D9098F50B10713FD54607815F18FAB8: Html.Exploit.CVE_2012_3993-1 FOUND
/mnt/partition/Users/Peter/AppData/Local/Temp/svchost.exe: Win.Trojan.Xtreme-7 FOUND
/mnt/partition/Users/Peter/AppData/Roaming/EpUpdate/bpd/BrowserPasswordDump.exe: Win.Dropper.Securityxploded-6871294-0 FOUND
/mnt/partition/Users/Peter/AppData/Roaming/EpUpdate/mmktz/mimikatz.exe: Win.Trojan.Mimikatz-6466236-0 FOUND
/mnt/partition/Users/Peter/AppData/Roaming/EpUpdate/mmktz/mimilib.dll: Win.Tool.Mimikatz-9784738-0 FOUND
/mnt/partition/Users/Peter/AppData/Roaming/EpUpdate/pwdump/PwDump7.exe: Win.Trojan.Pwdump-1 FOUND
/mnt/partition/Users/Peter/AppData/Roaming/HostData/update.exe: Win.Trojan.Xtreme-7 FOUND

----------- SCAN SUMMARY -----------
Known viruses: 8798148
Engine version: 0.98.7
Scanned directories: 18803
Scanned files: 117500
Infected files: 8
Data scanned: 8081.59 MB
Data read: 12881.35 MB (ratio 0.63:1)
Time: 2114.496 sec (35 m 14 s)
```

Resultat : 

* Un fichier dans firefox vulnérable à la __CVE-2012-3993__
* Un fichier cache dans INetCache contient un __Win.Trojan.Xtrem-7__
* L'__update.exe__ suspecté est bien infecté par le __Win.Trojan.Xtrem-7__
* Un fichier __BrowserPasswordDump.exe__ infecté par un __Win.Trojan.Pwdump-1__ trouvé dans le dossier EpUpdate. 

Le fichier __update.exe__ est impliqué.
Nous allons observer avec autopsy les fichiers, notament le dossier EpUpdate / INetCache et HostData\update.exe

* __EpUpdate__

```text
bpd/ - BrowserPasswordDump.exe
mmktz/ - mimikatz
nircmd/ – NirCmd
nmap/ - Nmap
pwdump/ - Pwdump
ssh/ - plink, pscp
thc/ - THC Hydra
passwords.txt – une wordlist de mot de passe
wdigest.reg – un outil pour modifier les registres
```

* __HostData/update.exe__

```text
 	File Name 	   	Modified/Written Time 	   	    Access Time 	   	            Change Time 	   	            Create Time
  	update.exe 	   	2005-06-03 07:01:04 (GMT) 	   	2005-06-03 07:01:04 (GMT) 	   	2016-08-16 13:03:04 (GMT) 	   	2005-06-03 07:01:04 (GMT)
```

Le fichier a bien été modifié le 2016-08-16 13:03:04.

* __INetCacheIE/R81B6P1C/3568226350[1].exe__


```text
000088D0:  5800 5400 5200 4500 4D00 4500 0D00 4900    X.T.R.E.M.E...I.
```
On retrouve dans la vue Hexa la signature du RAT : __XTREME__ ainsi que methode __URLDownloadToFile__

```text
0000EE10:  7957 0000 5552 4C44 6F77 6E6C 6F61 6454    yW..URLDownloadT
0000EE20:  6F46 696C 6557 0000 4368 6172 4E65 7874    oFileW
```

On peut présumer que le RAT xtrem a été téléchargé depuis le navigateur firefox.

## Historique de firefox

L'historique de navigation de firefox se trouve ici : __C:/Users/Peter/AppData/Local/Mozilla/Firefox/Profiles/Peter/places.sqlite__.

Nous allons utiliser l'outil __BrowsingHistoryView.exe.__ pour analyser l'historique de navigation.

```bash
wine BrowsingHistoryView.exe
```

L'utilisateur a visiter quelques sites le jours de l'attaque : 

* reddit
* skype
* msn
* blog.mycompany.ex

Aucune information sur le téléchargement d'un quelconque fichier ... Allons voir dans le cache.

```text
cd /mnt/partition/Users/Peter/AppData/Local/Mozilla/Firefox/Profiles/z0l7z3kd.default/cache2 

head index
pd=���4�Y�,$X�z���|�<��K|����
�B�i	珦���)�N�_�!<�!�������E�/�~
```

C'est un binaire ... Utilisons l'outil __MZCacheView__

L'analyse du site de l'enteprise montre une requete en javascript qui pointe vers __http://blog.mysportclub.ex/wpcontent/uploads/hk/task/opspy/index.php.__. Probablement infecté ! 

On remarque de multiple iframe imbriquées pointant vers différents liens, tous du site __blog.mysportclub.ex__
Ce sont des test de vulnérabilités.

C'est de là que le service svchost a été téléchargé puis lancé (xtrem RAT).

# Partie 4

__Timeline (jour/heures/minutes secondes) de ce qu'il se passe sur la machine infectée (pensez à renvoyer en annotation pour chaque étape de la timeline la preuve trouvée durant la dead analysys, soit via volatility, soit via caine sur le dump de disque).__

* Création __D:/Users/Peter/AppData/Roaming/HostData/update.exe__ 

> ```Tue  Aug 16 2016 13:02:57 	: 86	macb	r/r--x--x--x	0	0	101287-48-2	D:/Users/Peter/AppData/Roaming/HostData/update.exe ($FILE_NAME)```

| Heure    | description | source | 
| :------: | :---------: | :----: |
| 12:54:24 | Demarrage du premier process (boot pc) | Volatility |
| 13:02:46 | Peter se rends sur la page http://blog.mycompany.ex/ | Historique firefox |
| 13:03:17 | Redirection vers http://blog.mysportclub.ex et téléchargement du malware en cache | Historique firefox & analyse du cache |
| 13:02:53 | Création du fichier cache contenant le malware XTREM | analyse du cache & ClamAV analyse |
| 13:02:57 | Démarage du service svchost.exe contenant le RAT | Volatility |
| 13:03:04 | Démarage d'un deuxième explorer.exe| Volatility |
| 13:03:04 | Démarage de update.exe| volatility |
| 13:07:36 | Démarrage de plusieurs processus cmd.exe | |
| 13:14:47 | Création du dossier EpUpdate| Autopsy et analyse de fichier |

# Partie 5 

__Conclusion A : Que faudrait il faire pour nettoyer cet ordinateur?__

* Supprimer tous les fichier infectés et ajoutés par l'attaquant
* Supprimer le cache dans Firefox
* Mettre à jour Firefox et toutes les applications du PC

# Partie 6

__Conclusion B:As t'on des indices suffisants pour dire qu'il y a eu exfiltration de données, si oui, quels indices, et quelles données? Si non, y a t'il des indices qui peuvent aider à savoir si des données ont été exfiltrées.__

* Au vu des résultats que l'on a obtenu, on peut prétendre que des données ont étés exfiltrées, de pars les multiples requêtes vers des hôtes inconnues et le nombre d'outil serveur à de l'audit trouvés dans le dossier __EpUpdate__. Il faudrait regarder les logs réseaux, dans le SO (si il y en a un) pour voir ce qui a transité.

# Partie 7

__Conclusion C: Que préconisez-vous de faire pour que cette attaque ne puisse plus se reproduire sur d'autres ordinateurs de l'entreprise? On pourra imaginer tout ce que vous voulez, du moment que ce n'est pas une usine a gas ingérable.__

* L'installation d'un IDS/NSM tel que Security Onion. Complexe mais efficace.
* Sinon, un anti-virus aurait probablement détecté le RAT Extrem.
* De nombreux routeurs font de l'IDS/IPS
* Un serveur syslog est toujours un bon points pour garder des traces.