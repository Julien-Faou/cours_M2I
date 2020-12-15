#!/bin/bash

scripthelp() {
    echo "Usage: $0 [-h,-n]" >&2
    echo
    echo "   -h           print this help"
    echo "   -n XX        folder number"
    echo
    exit 1
}

startnetcat() {
   echo $(date)": un listener a été ouvert pour le dossier $number" >> log.txt
   nc -k -l -d localhost 1234 | while read line
   do
      echo $line >> ./$number/case.log 2>&1
   done
   #debuter_listener_file.sh($number)
}

folder() {
   [[ -d "./$number" ]] || mkdir ./$number
   echo "Demarrage du dossier $number"
   startnetcat &
}

$number
while getopts ':n:h' option; do
   case "$option" in
      h) scripthelp
         exit
         ;;
      n) number=$OPTARG
         [[ $number =~ '^[0-9]+$' ]] && scripthelp || folder
         ;;
      *) scripthelp
         exit 1
         ;;
   esac
done