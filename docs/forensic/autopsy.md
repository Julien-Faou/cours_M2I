# Autopsy

## start
```
sudo autopsy
```

```
http://localhost:9999/autopsy
```

Les fichiers finissant par E** => Fichier créé par le logiciel EnCase


* Suivre les étapes 

## Analyse d'une clé USB

1) A qui est cette clé ? 

```
Volume Label (Boot Sector): TERRYS WORK 
```

__Cette clé appartient à un certain "Terry" pour ses travaux__

2) Ya-t-il sur cette clé des exécutables ?

__Oui il y en a :__

* R54402.exe => Logiciel propriétaire DELL pour des drivers
* vnc-4_1_3-x86_win32.exe => Logiciel de prise de controle a distance
* xpadvancedkeylogger.exe  => Développé par Eltima Software


3) Si oui sont-ils corrompus ? 

* xpadvancedkeylogger.exe => __html__

### Virus total

* R54402.exe => R.A.S
* vnc-4_1_3-x86_win32.exe => 9 antivirus signal une menace, remote admin, me semble normal (faux positif)

4) Y a-t-il des images inappropriées ?

### Liste d'images
* _M57biz.jpg

5) A quoi servait cette clé ?



## Notes

* Liste d'url
* Keylogger
* patentauto.py

```
# Summary: MozRepl needs to telnet to the browser via port 4242.  Once connected the port can program
# can issue commands directly to the web browser.  This program gets the list of urls from the text file.
# Then randomly picks a URL and surfs it for background noise.
```

```
if __name__ == "__main__":
    while(1):
        hour = time.localtime()[3]
        if (hour >= 9 and hour < 10) or (hour >= 14 and hour < 14) or (hour >= 16 and hour < 17):
            print "Visiting Persona URLs..."
            urlMain()
        if (hour >= 10 and hour < 12) or (hour >= 13 and hour < 16):
            print "Patent Searching..."
            patentMain()
```

__Fonction étrange avec les horraires__


* credentials
```

<BR>

<b><font size="1" face="Verdana">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font></b>

<font face="Verdana" color="#000000" size="2">m57admin(EditBox)</font>

<BR>

<b><font size="1" face="Verdana">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font></b>

<b><font face="Verdana" color="#000000" size="2">admin01(Password EditBox)</font></b>

<BR>

<b><font size="1" face="Verdana">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font></b>

<a hre

```