#!/bin/bash

echo "Fin des operations à $(date +%y/%m/%d%H:%M:%S)" | nc localhost 1234

killall debuter_listener_file.sh
killall debuter_audit.sh
killall nc