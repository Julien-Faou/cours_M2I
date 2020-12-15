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
    while read filename
    do
        mkdir -p $number
        nc -k -l localhost 1236 | while read line
        do
            echo $line >> $number/$(basename $filename) 2>&1
        done
    done < <(nc -l localhost 1235)

}

$number
while getopts ':n:h' option; do
   case "$option" in
      h) scripthelp
         exit
         ;;
      n) number=$OPTARG
         [[ $number =~ '^[0-9]+$' ]] && scripthelp
         startnetcat
         ;;
      *) scripthelp
         exit 1
         ;;
   esac
done


