#!/bin/bash

cadena="Los archivos son iguales :D"
python3 test.py
output=$(python3 backup.py 2>&1)
echo "$(date) : $output" >> status.log
if [ "$output" == "$cadena" ]
then
    exit 1
else
    echo "Actualizando los datos a Github :3"
    git add banlist.txt
    git commit -m "Actualizacion base de datos"
    git push origin main

fi
